export interface TelemetryEvent {
    installation_id: string;
    timestamp: string;
    framework: string;
    framework_version: string;
    platform: string;
    platform_details?: object;
}