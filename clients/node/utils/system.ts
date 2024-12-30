import * as os from 'os';
import { System } from '../interfaces/system.interface';

export const SystemData = (): System => {
    const systemData = {}
    try {
        return {
            platform: `${os.type()} ${os.release()}`,
            arch: os.arch(),
        };
    } catch {
        return {platform: 'Unknown', arch: 'N/A'};
    }
}