import { resolve } from 'path'
import { sveltekit } from '@sveltejs/kit/vite'

/** @type {import('vite').UserConfig} */
const config = {
  plugins: [sveltekit()],
  resolve: {
    alias: {
      $styles: resolve('./src/styles'),
      $components: resolve('./src/components')
    }
  }
}

export default config
