package ch.ethz.seb.sebserver.gbl.model.exam;
/**
 * Test stand-in carrying only the fields the validator reads. Field names and the
 * two built-in enum values are copied verbatim from seb-server @ master; the
 * BIGBLUEBUTTON value is the one-line enum addition the fix assumes.
 */
public class ProctoringServiceSettings {

    public enum ProctoringServerType {
        JITSI_MEET,
        ZOOM,
        BIGBLUEBUTTON
    }

    public final ProctoringServerType serverType;
    public final String serverURL;
    public final String appKey;
    public final String appSecret;
    public final String accountId;
    public final String clientId;
    public final String clientSecret;
    public final String sdkKey;
    public final String sdkSecret;

    public ProctoringServiceSettings(
            final ProctoringServerType serverType,
            final String serverURL,
            final String appKey,
            final String appSecret,
            final String accountId,
            final String clientId,
            final String clientSecret,
            final String sdkKey,
            final String sdkSecret) {
        this.serverType = serverType;
        this.serverURL = serverURL;
        this.appKey = appKey;
        this.appSecret = appSecret;
        this.accountId = accountId;
        this.clientId = clientId;
        this.clientSecret = clientSecret;
        this.sdkKey = sdkKey;
        this.sdkSecret = sdkSecret;
    }
}
