package ch.ethz.seb.sebserver.webservice.servicelayer.validation;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;
import org.apache.commons.lang3.StringUtils;
import ch.ethz.seb.sebserver.gbl.model.exam.ProctoringServiceSettings;
import ch.ethz.seb.sebserver.gbl.model.exam.ProctoringServiceSettings.ProctoringServerType;

/**
 * Logic-faithful copy of seb-server's ProctoringSettingsValidator @ master
 * (webservice/servicelayer/validation/ProctoringSettingsValidator.java), kept in
 * the test tree ONLY so the test can demonstrate gap 90 by execution rather than
 * by assertion. Note the final `return true`.
 */
public class OriginalProctoringSettingsValidator
        implements ConstraintValidator<ValidProctoringSettings, ProctoringServiceSettings> {

    @Override
    public boolean isValid(final ProctoringServiceSettings value, final ConstraintValidatorContext context) {
        if (value == null) { return false; }

        if (value.serverType == ProctoringServerType.JITSI_MEET || value.serverType == ProctoringServerType.ZOOM) {
            boolean passed = true;
            if (StringUtils.isBlank(value.serverURL)) { violate(context, "serverURL"); passed = false; }
            if (value.serverType == ProctoringServerType.JITSI_MEET) {
                if (StringUtils.isBlank(value.appKey)) { violate(context, "appKey"); passed = false; }
                if (StringUtils.isBlank(value.appSecret)) { violate(context, "appSecret"); passed = false; }
            }
            if (value.serverType == ProctoringServerType.ZOOM) {
                if (StringUtils.isBlank(value.accountId)) { violate(context, "accountId"); passed = false; }
                if (StringUtils.isBlank(value.clientId)) { violate(context, "clientId"); passed = false; }
                if (StringUtils.isBlank(value.clientSecret)) { violate(context, "clientSecret"); passed = false; }
                if (StringUtils.isBlank(value.sdkKey)) { violate(context, "sdkKey"); passed = false; }
                if (StringUtils.isBlank(value.sdkSecret)) { violate(context, "sdkSecret"); passed = false; }
            }
            return passed;
        }

        return true; // <-- gap 90
    }

    private void violate(final ConstraintValidatorContext context, final String field) {
        context.disableDefaultConstraintViolation();
        context.buildConstraintViolationWithTemplate("proctoringSettings:" + field + ":notNull")
                .addPropertyNode(field).addConstraintViolation();
    }
}
