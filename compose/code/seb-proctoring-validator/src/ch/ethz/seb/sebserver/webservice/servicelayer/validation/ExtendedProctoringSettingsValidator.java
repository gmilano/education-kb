/*
 * Drop-in replacement for ProctoringSettingsValidator (SafeExamBrowser/seb-server,
 * Apache-2.0) that closes gap 90: SEB Server's own validator checks fields only
 * for JITSI_MEET and ZOOM and then falls through to `return true`, so ANY
 * third-party ProctoringServerType is accepted with its credential fields empty.
 *
 * Two changes, both deliberate:
 *   1. BIGBLUEBUTTON is validated like the two built-in providers, with the same
 *      `proctoringSettings:<field>:notNull` violation templates, so the existing
 *      UI/i18n keys keep working unchanged.
 *   2. The fall-through FAILS CLOSED. An unrecognised serverType is rejected with
 *      `proctoringSettings:serverType:typeNotSupported` instead of being accepted.
 *      This is the actual fix: without it, every future enum value silently
 *      re-opens the same hole.
 */
package ch.ethz.seb.sebserver.webservice.servicelayer.validation;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;

import org.apache.commons.lang3.StringUtils;

import ch.ethz.seb.sebserver.gbl.model.exam.ProctoringServiceSettings;
import ch.ethz.seb.sebserver.gbl.model.exam.ProctoringServiceSettings.ProctoringServerType;

public class ExtendedProctoringSettingsValidator
        implements ConstraintValidator<ValidProctoringSettings, ProctoringServiceSettings> {

    @Override
    public boolean isValid(final ProctoringServiceSettings value, final ConstraintValidatorContext context) {
        if (value == null) {
            return false;
        }

        if (value.serverType == null) {
            return reject(context, "serverType", "notNull");
        }

        // Every provider needs a server URL.
        boolean passed = true;
        if (StringUtils.isBlank(value.serverURL)) {
            passed = reject(context, "serverURL", "notNull");
        }

        switch (value.serverType) {
            case JITSI_MEET:
                if (StringUtils.isBlank(value.appKey)) {
                    passed = reject(context, "appKey", "notNull");
                }
                if (StringUtils.isBlank(value.appSecret)) {
                    passed = reject(context, "appSecret", "notNull");
                }
                return passed;

            case ZOOM:
                if (StringUtils.isBlank(value.accountId)) {
                    passed = reject(context, "accountId", "notNull");
                }
                if (StringUtils.isBlank(value.clientId)) {
                    passed = reject(context, "clientId", "notNull");
                }
                if (StringUtils.isBlank(value.clientSecret)) {
                    passed = reject(context, "clientSecret", "notNull");
                }
                if (StringUtils.isBlank(value.sdkKey)) {
                    passed = reject(context, "sdkKey", "notNull");
                }
                if (StringUtils.isBlank(value.sdkSecret)) {
                    passed = reject(context, "sdkSecret", "notNull");
                }
                return passed;

            case BIGBLUEBUTTON:
                // BBB authenticates API calls with a single shared secret, carried
                // in appSecret. appKey/accountId/sdk* are not part of its contract,
                // so they are NOT required — requiring them would be a false
                // constraint, which is its own kind of wrong data.
                if (StringUtils.isBlank(value.appSecret)) {
                    passed = reject(context, "appSecret", "notNull");
                }
                return passed;

            default:
                // Fail closed. This is the gap-90 fix.
                return reject(context, "serverType", "typeNotSupported");
        }
    }

    private boolean reject(
            final ConstraintValidatorContext context,
            final String field,
            final String reason) {

        context.disableDefaultConstraintViolation();
        context
                .buildConstraintViolationWithTemplate("proctoringSettings:" + field + ":" + reason)
                .addPropertyNode(field).addConstraintViolation();
        return false;
    }
}
