import { defineConfig } from 'vitepress'
import { generateSidebar } from 'vitepress-sidebar'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Hishiro64/home-server",
  description: "A repo site for Home-Server",
  base: '/home-server/',
  cleanUrls: true,
  sitemap: {
      hostname: 'https://hishiro64.github.io/home-server'
    },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Docs', link: '/1_Raspberry Pi OS Image Configuration.md' }
    ],

    sidebar: generateSidebar({
      documentRootPath: '/',
      collapsed: false,
      useTitleFromFileHeading: true,
      capitalizeFirst: true,
      //useFolderTitleFromIndexFile: true
      // Custom ordering
      sortMenusByName: false,
      manualSortFileNameByPriority: [
        '1_Raspberry Pi OS Image Configuration.md',
        'about.md'
      ]

    }),

    // enable search
    search: {
      provider: 'local'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/hishiro64' }
    ]
  }
})