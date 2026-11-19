<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script>
export default {
  computed: {
    layout() {
      return this.$route.meta.layout || "base-layout";
    },
  },
};
</script>

<style lang="scss">
:root {
  --farm-header-height: 72px;
}

@media (max-width: 600px) {
  :root {
    --farm-header-height: 62px;
  }
}

@font-face {
  font-family: "Tilda Sans Regular";
  src: url("/fonts/tilda-sans-regular.ttf") format("truetype");
  font-display: swap;
}

@font-face {
  font-family: "Tilda Sans Bold";
  src: url("/fonts/tilda-sans-bold.ttf") format("truetype");
  font-display: swap;
}

@font-face {
  font-family: "Tilda Sans Black";
  src: url("/fonts/tilda-sans-black.ttf") format("truetype");
  font-display: swap;
}

html,
body,
#app {
  height: 100%;
  margin: 0;
  background-color: #fdf0d5;
  overflow: hidden;
}

body {
  color: #0d1821;
  font-family: "Tilda Sans Regular", sans-serif !important;
}

.q-page-container {
  height: 100dvh;
  overflow: hidden;
}

.farm-page {
  height: calc(100dvh - var(--farm-header-height));
  min-height: 0 !important;
  overflow: hidden;
}

.farm-list-page {
  display: flex;
  flex-direction: column;
}

.farm-bounded-table {
  max-height: 100%;
  min-height: 0;
}

.farm-bounded-table .q-table__middle {
  min-height: 0;
  overflow: auto;
}

.farm-bounded-table thead th {
  position: sticky;
  top: 0;
  z-index: 1;
  background: #0d1821;
  color: #fdf0d5;
}

.q-page .q-card,
.q-page .q-table__container,
body .q-table__container.fullscreen {
  background: #fdf0d5;
  color: #0d1821;
  border: 2px solid #0d1821;
  border-radius: 0;
  box-shadow: none;
}

.q-card .text-h6,
.q-table__container .text-h6 {
  font-family: "Tilda Sans Bold", sans-serif;
}

.q-table thead tr {
  background: #0d1821;
  color: #fdf0d5;
}

.q-table__container .q-table__middle {
  overflow-x: auto;
}

.q-page .q-field--outlined .q-field__control {
  background: #fdf0d5;
  border-radius: 0;
  padding: 0 8px;
}

.flags-filter-form .q-field {
  min-height: 56px;
}

.q-page .q-field--dense:not(.q-textarea) .q-field__control,
.q-page .q-field--dense:not(.q-textarea) .q-field__marginal {
  min-height: 36px;
  height: 36px;
}

.q-page .q-field--outlined .q-field__control::before,
.q-page .q-field--outlined .q-field__control::after {
  border: 2px solid #0d1821;
}

.q-field,
.q-btn,
.q-table,
.q-menu {
  font-family: "Tilda Sans Regular", sans-serif;
}

.q-page .q-field__label,
.q-page .q-field__native,
.q-page .q-field__input {
  font-size: 12.8px;
}

.q-page .flags-filter-form .empty-select .q-field__native {
  color: #77736c;
}

.q-btn.bg-primary {
  border: 2px solid #0d1821;
  border-radius: 0;
  box-shadow: 3.2px 3.2px 0 #eca72c;
  color: #fdf0d5;
  font-family: "Tilda Sans Bold", sans-serif;
  font-size: 12.8px;
}

.q-menu {
  background: #fdf0d5;
  border: 2px solid #0d1821;
  border-radius: 0;
  box-shadow: none;
}

</style>
