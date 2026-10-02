package javax.validation;
import java.util.ArrayList;
import java.util.List;
/** Recording test stand-in: captures the violation templates the validator builds. */
public class ConstraintValidatorContext {
    public final List<String> templates = new ArrayList<>();
    public final List<String> propertyNodes = new ArrayList<>();
    public int defaultDisabledCount = 0;

    public void disableDefaultConstraintViolation() { this.defaultDisabledCount++; }

    public Builder buildConstraintViolationWithTemplate(final String template) {
        this.templates.add(template);
        return new Builder();
    }

    public class Builder {
        public Builder addPropertyNode(final String node) {
            ConstraintValidatorContext.this.propertyNodes.add(node);
            return this;
        }
        public void addConstraintViolation() { /* recorded above */ }
    }
}
