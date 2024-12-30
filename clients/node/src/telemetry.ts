import { TelemetryEvent } from '../interfaces/telemetry.interface';
import { sendTelemetryEvent } from '../utils/fetch';
import { detectFramework } from '../utils/framework';
import { SystemData } from '../utils/system';

/**
 * **Metryflow** for NodeJS
 * 
 * @abstract Metryflow telemetry data collection for NodeJS.
 *
 * @documentation https://github.com/rperezll/metryflow
 * @param {Object} [config] - Optional configuration object for debugging.
 * @param {boolean} [config.debug] - If true, logs the telemetry event to the console.
 * 
 */
export const Metriflow = async (config?: { debug: boolean }) => {
  const system = await SystemData();
  const framework = await detectFramework();

  const telemetryEvent: TelemetryEvent = {
    installation_id: "",
    timestamp: new Date().toISOString(),
    framework: framework.framework,
    framework_version: framework.version,
    platform: system.platform,
    platform_details: { arch: system.arch },
  };

  if (config?.debug) console.log('Telemetry Event:', telemetryEvent);
  await sendTelemetryEvent(telemetryEvent);
};



Metriflow();
