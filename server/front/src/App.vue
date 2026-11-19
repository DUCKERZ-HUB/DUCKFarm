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
  --farm-bg: #fdf0d5;
  --farm-text: #0d1821;
  --farm-border: #0d1821;
  --farm-table-head: #0d1821;
  --farm-table-head-text: #fdf0d5;
  --farm-action-bg: #0d1821;
  --farm-action-text: #fdf0d5;
  --farm-muted: #77736c;
  --farm-divider: rgba(13, 24, 33, 0.15);
}

:root[data-theme="dark"] {
  color-scheme: dark;
  --farm-bg: #0c1f2f;
  --farm-text: #e3d8bf;
  --farm-border: #e3d8bf;
  --farm-table-head: #e3d8bf;
  --farm-table-head-text: #0c1f2f;
  --farm-action-bg: #e3d8bf;
  --farm-action-text: #0c1f2f;
  --farm-muted: #b7ad9a;
  --farm-divider: rgba(227, 216, 191, 0.25);
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
  background-color: var(--farm-bg);
  overflow: hidden;
}

body {
  color: var(--farm-text);
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
  background: var(--farm-table-head);
  color: var(--farm-table-head-text);
}

.q-page .q-card,
.farm-form-dialog .q-card,
body .q-table__container.fullscreen .q-card,
.q-page .q-table__container,
body .q-table__container.fullscreen {
  background: var(--farm-bg);
  color: var(--farm-text);
  border: 2px solid var(--farm-border);
  border-radius: 0;
  box-shadow: none;
}

.farm-form-dialog {
  width: min(90vw, 760px);
  max-height: calc(100dvh - 32px);
  overflow-y: auto;
}

.q-card .text-h6,
.q-table__container .text-h6 {
  font-family: "Tilda Sans Bold", sans-serif;
}

.q-table thead tr {
  background: var(--farm-table-head);
  color: var(--farm-table-head-text);
}

.farm-table-header {
  background: var(--farm-table-head) !important;
  color: var(--farm-table-head-text) !important;
}

.q-table th,
.q-table td,
.q-table__top,
.q-table__bottom {
  border-color: var(--farm-divider);
}

.q-table__container .q-table__middle {
  overflow-x: auto;
}

:is(.q-page, .farm-form-dialog) .q-field--outlined .q-field__control {
  background: var(--farm-bg);
  border-radius: 0;
  padding: 0 8px;
}

.flags-filter-form .q-field {
  min-height: 56px;
}

:is(.q-page, .farm-form-dialog) .q-field--dense:not(.q-textarea) .q-field__control,
:is(.q-page, .farm-form-dialog) .q-field--dense:not(.q-textarea) .q-field__marginal {
  min-height: 36px;
  height: 36px;
}

:is(.q-page, .farm-form-dialog) .q-field--outlined .q-field__control::before,
:is(.q-page, .farm-form-dialog) .q-field--outlined .q-field__control::after {
  border: 2px solid var(--farm-border);
}

.q-field,
.q-btn,
.q-table,
.q-menu {
  font-family: "Tilda Sans Regular", sans-serif;
}

:is(.q-page, .farm-form-dialog) .q-field__label,
:is(.q-page, .farm-form-dialog) .q-field__native,
:is(.q-page, .farm-form-dialog) .q-field__input {
  font-size: 12.8px;
}

:is(.q-page, .farm-form-dialog) .flags-filter-form .empty-select .q-field__native {
  color: var(--farm-muted);
}

.q-btn.bg-primary {
  background: var(--farm-action-bg) !important;
  border: 2px solid var(--farm-border);
  border-radius: 0;
  box-shadow: 3.2px 3.2px 0 #eca72c;
  color: var(--farm-action-text) !important;
  font-family: "Tilda Sans Bold", sans-serif;
  font-size: 12.8px;
}

.q-menu {
  background: var(--farm-bg) !important;
  color: var(--farm-text) !important;
  border: 2px solid var(--farm-border);
  border-radius: 0;
  box-shadow: none;
}

:root[data-theme="dark"] .q-menu .q-item:hover {
  background: #253644;
}

:root[data-theme="dark"] .q-field__native,
:root[data-theme="dark"] .q-field__input,
:root[data-theme="dark"] .q-field__append,
:root[data-theme="dark"] .q-field__marginal,
:root[data-theme="dark"] .q-field__bottom {
  color: var(--farm-text);
}

:root[data-theme="dark"] input::placeholder,
:root[data-theme="dark"] textarea::placeholder {
  color: var(--farm-muted);
  opacity: 1;
}

:root[data-theme="dark"] .q-table tbody tr:hover {
  background: #253644;
}

</style>
