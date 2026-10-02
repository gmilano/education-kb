package javax.validation;
/** Test stand-in for the Bean Validation interface (javax.validation:validation-api). */
public interface ConstraintValidator<A extends java.lang.annotation.Annotation, T> {
    boolean isValid(T value, ConstraintValidatorContext context);
}
