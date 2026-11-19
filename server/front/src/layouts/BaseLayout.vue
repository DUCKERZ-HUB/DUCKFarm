<template>
  <q-layout view="hHh lpR fFf">
    <q-header class="farm-header">
      <q-toolbar class="farm-toolbar">
        <img class="farm-logo" src="/duckfarm-logo.svg" alt="DUCKFARM" />
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
      </q-toolbar>
    </q-header>

    <q-page-container>
      <slot />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "BaseLayout",
};
</script>

<style scoped>
.farm-header {
  background: #fdf0d5;
  color: #0d1821;
  border-bottom: 2px solid #0d1821;
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
  color: #0d1821;
  font-family: "Tilda Sans Black", sans-serif;
  font-size: 16px;
  line-height: normal;
  text-decoration: none;
  white-space: nowrap;
  transition: background-color 0.3s, color 0.3s, box-shadow 0.3s;
}

.farm-nav__item--active,
.farm-nav__item:hover {
  background: #0d1821;
  color: #fdf0d5;
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
}
</style>
