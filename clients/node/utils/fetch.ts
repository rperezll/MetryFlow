import { TelemetryEvent } from "../interfaces/telemetry.interface";

export const sendTelemetryEvent = async (event: TelemetryEvent): Promise<void> => {
    try {
        const response = await fetch('http://localhost:8000/telemetry/events', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(event),
        });

        if (!response.ok) console.error('Telemetry send error:', response.statusText);
        else console.log('Telemetry sent successfully');
    } catch (error) {
        console.error('Telemetry request error:', error);
    }
};