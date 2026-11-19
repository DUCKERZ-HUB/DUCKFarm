<template>
  <q-layout view="hHh lpR fFf">
    <q-header class="farm-header">
      <q-toolbar class="farm-toolbar">
        <img
          class="farm-logo"
          :src="darkTheme ? '/duckfarm-logo-dark.svg' : '/duckfarm-logo.svg'"
          alt="DUCKFARM"
        />
        <nav class="farm-nav" aria-label="DUCKFarm navigation">
          <router-link
            class="farm-nav__item"
            exact-active-class="farm-nav__item--active"
            :to="{ name: 'flags' }"
          >FLAGS</router-link>
          <router-link
            class="farm-nav__item"
            exact-active-class="farm-nav__item--active"
            :to="{ name: 'teams' }"
          >TEAMS</router-link>
          <router-link
            class="farm-nav__item"
            exact-active-class="farm-nav__item--active"
            :to="{ name: 'sploits' }"
          >SPLOITS</router-link>
        </nav>
        <button
          class="theme-toggle"
          type="button"
          :aria-label="darkTheme ? 'Switch to light theme' : 'Switch to dark theme'"
          :title="darkTheme ? 'Light theme' : 'Dark theme'"
          @click="toggleTheme"
        >
          <q-icon :name="darkTheme ? 'light_mode' : 'dark_mode'" size="20px" />
        </button>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <slot />
    </q-page-container>
  </q-layout>
</template>

<script>
import { setCssVar } from "quasar";

const THEME_KEY = "duckfarm-theme";

export default {
  name: "BaseLayout",
  data() {
    return {
      darkTheme: document.documentElement.dataset.theme === "dark",
    };
  },
  mounted() {
    this.applyTheme(this.darkTheme);
  },
  methods: {
    applyTheme(darkTheme) {
      document.documentElement.dataset.theme = darkTheme ? "dark" : "light";
      setCssVar("primary", darkTheme ? "#e3d8bf" : "#0d1821");
    },
    toggleTheme() {
      this.darkTheme = !this.darkTheme;
      this.applyTheme(this.darkTheme);
      try {
        window.localStorage.setItem(THEME_KEY, this.darkTheme ? "dark" : "light");
      } catch (_) {
        // Keep the current theme even if storage is unavailable.
      }
    },
  },
};
</script>

<style scoped>
.farm-header {
  background: var(--farm-bg);
  color: var(--farm-text);
  border-bottom: 2px solid var(--farm-border);
  box-shadow: none;
}

.farm-toolbar {
  min-height: 70px;
  max-width: 1120px;
  margin: 0 auto;
  padding: 8px 16px;
}

.farm-logo {
  display: block;
  width: 270px;
  height: auto;
}

.farm-nav {
  display: flex;
  align-items: center;
  margin-left: auto;
}

.farm-nav__item {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 8px;
  padding: 8px;
  color: var(--farm-text);
  font-family: "Tilda Sans Black", sans-serif;
  font-size: 16px;
  line-height: normal;
  text-decoration: none;
  white-space: nowrap;
  transition: background-color 0.3s, color 0.3s, box-shadow 0.3s;
}

.farm-nav__item--active,
.farm-nav__item:hover {
  background: var(--farm-text);
  color: var(--farm-bg);
}

.theme-toggle {
  display: inline-flex;
  flex: 0 0 auto;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  margin-left: 8px;
  padding: 0;
  color: var(--farm-text);
  background: transparent;
  border: 1px solid var(--farm-border);
  cursor: pointer;
}

.theme-toggle:hover {
  color: var(--farm-bg);
  background: var(--farm-text);
}

.farm-nav__item:first-child:is(.farm-nav__item--active, :hover) {
  box-shadow: 3.2px 3.2px 0 #b80c09;
}

.farm-nav__item:nth-child(2):is(.farm-nav__item--active, :hover) {
  box-shadow: 3.2px 3.2px 0 #5fad56;
}

.farm-nav__item:nth-child(3):is(.farm-nav__item--active, :hover) {
  box-shadow: 3.2px 3.2px 0 #eca72c;
}

.farm-nav__item:focus-visible {
  outline: 2px solid #b80c09;
  outline-offset: 4px;
}

@media (max-width: 600px) {
  .farm-toolbar {
    min-height: 60px;
    padding: 6px 12px;
  }

  .farm-logo {
    width: 125px;
  }

  .farm-nav__item {
    margin-right: 2px;
    padding: 5px;
    font-size: 12px;
  }

  .theme-toggle {
    width: 28px;
    height: 28px;
    margin-left: 4px;
  }
}
</style>
