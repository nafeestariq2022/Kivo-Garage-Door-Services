import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://kivogaragedoorservices.us',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
  outDir: './dist',
  build: {
    format: 'directory',
  }
});
