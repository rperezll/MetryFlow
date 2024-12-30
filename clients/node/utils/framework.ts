import * as fs from 'fs';
import { resolve } from 'path';
import { readFile } from 'fs/promises';
import { Framework } from "../interfaces/framework.interface";

export const detectFramework = async (): Promise<Framework> => {
  if (fs.existsSync('astro.config.mjs') || fs.existsSync('astro.config.ts')) return await getFrameworkVersion('astro');
  if (fs.existsSync('next.config.js')) return await getFrameworkVersion('next');
  if (fs.existsSync('server.js') || fs.existsSync('app.js')) return await getFrameworkVersion('express');
  return { framework: 'Unknown', version: 'N/A' };
};

export const getFrameworkVersion = async (framework: string): Promise<Framework> => {
  try {
    const packagePath = resolve('node_modules', framework, 'package.json');
    const packageJson = JSON.parse(await readFile(packagePath, 'utf-8'));
    return { framework: framework.charAt(0).toUpperCase() + framework.slice(1), version: packageJson.version };
  } catch {
    return { framework, version: 'N/A' };
  }
};