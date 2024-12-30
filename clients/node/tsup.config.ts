import { defineConfig } from 'tsup';

export default defineConfig({
  entry: ['src/telemetry.ts'],
  format: ['cjs', 'esm'],
  target: 'node20',
  sourcemap: true,
  dts: {
    entry: 'src/telemetry.ts',
    compilerOptions: {
      module: "esnext",
      resolveJsonModule: true,
      moduleResolution: 'node',
    },
  },
  clean: true,
  outDir: 'dist',
});