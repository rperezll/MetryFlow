import type { AstroIntegration } from 'astro';
import { Metriflow } from 'metryflow-node';

/**
 * **Metryflow** for Astro
 * 
 * @abstract Metryflow telemetry data collection for Astro.
 *
 * @documentation https://github.com/rperezll/metryflow
 * @param {Object} [config] - Optional configuration object for debugging.
 * @param {boolean} [config.debug] - If true, logs the telemetry event to the console.
 * 
 */
export const Metryflow = (config?: { debug: boolean } ): AstroIntegration => {
    return {
        name: 'metryflow',
        hooks: {
            // Dev mode
            'astro:server:setup': async () => {
                await Metriflow();
            },
            // Prod mode
            'astro:build:start': async () => {
                await Metriflow();
            },
        },
    };
}