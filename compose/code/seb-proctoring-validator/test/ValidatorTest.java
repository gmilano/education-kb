import javax.validation.ConstraintValidatorContext;
import ch.ethz.seb.sebserver.gbl.model.exam.ProctoringServiceSettings;
import ch.ethz.seb.sebserver.gbl.model.exam.ProctoringServiceSettings.ProctoringServerType;
import ch.ethz.seb.sebserver.webservice.servicelayer.validation.ExtendedProctoringSettingsValidator;
import ch.ethz.seb.sebserver.webservice.servicelayer.validation.OriginalProctoringSettingsValidator;

/** Pase 43, action 3: prove gap 90 and prove the fix, both by execution. */
public class ValidatorTest {

    static int checks = 0;
    static int failed = 0;

    static void check(final boolean cond, final String label) {
        checks++;
        if (!cond) { failed++; }
        System.out.println("  " + (cond ? "ok  " : "FAIL") + "  " + label);
    }

    static ProctoringServiceSettings settings(
            final ProctoringServerType type, final String url, final String appKey,
            final String appSecret) {
        return new ProctoringServiceSettings(type, url, appKey, appSecret,
                null, null, null, null, null);
    }

    static ProctoringServiceSettings zoomComplete() {
        return new ProctoringServiceSettings(ProctoringServerType.ZOOM,
                "https://zoom.example.org", null, null,
                "acct", "cid", "csecret", "skey", "ssecret");
    }

    public static void main(final String[] args) {
        final OriginalProctoringSettingsValidator original =
                new OriginalProctoringSettingsValidator();
        final ExtendedProctoringSettingsValidator fixed =
                new ExtendedProctoringSettingsValidator();

        // ---- gap 90, demonstrated ----
        System.out.println("1. gap 90: the CURRENT validator accepts an empty third-party provider");
        final ProctoringServiceSettings emptyBbb =
                settings(ProctoringServerType.BIGBLUEBUTTON, null, null, null);
        ConstraintValidatorContext ctx = new ConstraintValidatorContext();
        final boolean originalVerdict = original.isValid(emptyBbb, ctx);
        check(originalVerdict, "original validator returns TRUE for BIGBLUEBUTTON with every field null");
        check(ctx.templates.isEmpty(), "original validator raised ZERO violations (" + ctx.templates.size() + ")");

        // ---- the fix rejects what the original accepted ----
        System.out.println("\n2. the fix REJECTS the same incomplete settings");
        ctx = new ConstraintValidatorContext();
        check(!fixed.isValid(emptyBbb, ctx), "fixed validator returns FALSE");
        check(ctx.templates.contains("proctoringSettings:serverURL:notNull"),
                "raised proctoringSettings:serverURL:notNull");
        check(ctx.templates.contains("proctoringSettings:appSecret:notNull"),
                "raised proctoringSettings:appSecret:notNull");
        check(ctx.propertyNodes.contains("serverURL") && ctx.propertyNodes.contains("appSecret"),
                "property nodes attached for both fields");
        check(ctx.defaultDisabledCount == ctx.templates.size(),
                "default constraint violation disabled once per violation ("
                        + ctx.defaultDisabledCount + "/" + ctx.templates.size() + ")");

        // ---- partially complete: url present, secret missing ----
        System.out.println("\n3. partially complete settings are still rejected, on the missing field only");
        ctx = new ConstraintValidatorContext();
        check(!fixed.isValid(settings(ProctoringServerType.BIGBLUEBUTTON,
                        "https://bbb.example.org", null, null), ctx),
                "url present, shared secret missing -> FALSE");
        check(ctx.templates.size() == 1
                        && ctx.templates.contains("proctoringSettings:appSecret:notNull"),
                "exactly one violation, on appSecret (" + ctx.templates + ")");

        // ---- blank, not just null ----
        System.out.println("\n4. whitespace counts as missing, not as a value");
        ctx = new ConstraintValidatorContext();
        check(!fixed.isValid(settings(ProctoringServerType.BIGBLUEBUTTON,
                        "   ", "  ", "\t"), ctx),
                "whitespace-only fields -> FALSE");

        // ---- complete settings accepted ----
        System.out.println("\n5. COMPLETE settings are accepted, with no violations");
        ctx = new ConstraintValidatorContext();
        check(fixed.isValid(settings(ProctoringServerType.BIGBLUEBUTTON,
                        "https://bbb.example.org", null, "shared-secret"), ctx),
                "complete BIGBLUEBUTTON settings -> TRUE");
        check(ctx.templates.isEmpty(), "no violations raised (" + ctx.templates + ")");
        check(ctx.defaultDisabledCount == 0, "default violation never disabled on the happy path");

        // ---- no regression on the two built-in providers ----
        System.out.println("\n6. no regression: the two built-in providers behave as before");
        ctx = new ConstraintValidatorContext();
        check(fixed.isValid(zoomComplete(), ctx) && ctx.templates.isEmpty(),
                "complete ZOOM settings still accepted");
        ctx = new ConstraintValidatorContext();
        check(!fixed.isValid(settings(ProctoringServerType.ZOOM, "https://z", null, null), ctx),
                "ZOOM missing accountId/clientId/... still rejected");
        check(ctx.templates.contains("proctoringSettings:accountId:notNull")
                        && ctx.templates.contains("proctoringSettings:sdkSecret:notNull"),
                "ZOOM violations use the same templates as before (" + ctx.templates.size() + " raised)");
        ctx = new ConstraintValidatorContext();
        check(fixed.isValid(settings(ProctoringServerType.JITSI_MEET,
                        "https://j", "key", "secret"), ctx) && ctx.templates.isEmpty(),
                "complete JITSI_MEET settings still accepted");
        ctx = new ConstraintValidatorContext();
        check(!fixed.isValid(settings(ProctoringServerType.JITSI_MEET, "https://j", null, null), ctx),
                "JITSI_MEET missing appKey/appSecret still rejected");

        // ---- null handling ----
        System.out.println("\n7. null settings and null serverType");
        check(!fixed.isValid(null, new ConstraintValidatorContext()), "null settings -> FALSE");
        ctx = new ConstraintValidatorContext();
        check(!fixed.isValid(settings(null, "https://x", "k", "s"), ctx), "null serverType -> FALSE");
        check(ctx.templates.contains("proctoringSettings:serverType:notNull"),
                "raised proctoringSettings:serverType:notNull");

        System.out.println("\n" + (checks - failed) + "/" + checks + " checks passed");
        if (failed > 0) {
            System.out.println("FAILED");
            System.exit(1);
        }
        System.out.println("ACTION 3 VERIFIED: gap 90 reproduced by execution, and the replacement "
                + "validator rejects\nincomplete third-party settings and accepts complete ones, "
                + "without regressing JITSI_MEET or ZOOM.");
    }
}
