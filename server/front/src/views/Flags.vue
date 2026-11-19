<template>
  <q-page class="q-pa-md farm-page flags-page">
    <div class="compact-actions">
      <q-btn label="Filter flags" color="primary" @click="filtersOpen = true" />
      <q-btn label="Submit manually" color="primary" @click="manualOpen = true" />
    </div>
    <div class="row justify-between q-col-gutter-md flags-controls">
      <div class="col-12"><flags-form /></div>
      <div class="col-12"><flags-submit /></div>
    </div>
    <div class="flags-list">
      <flags-table />
    </div>
    <q-dialog v-model="filtersOpen">
      <div class="farm-form-dialog">
        <flags-form @submitted="filtersOpen = false" />
      </div>
    </q-dialog>
    <q-dialog v-model="manualOpen">
      <div class="farm-form-dialog">
        <flags-submit @submitted="manualOpen = false" />
      </div>
    </q-dialog>
  </q-page>
</template>

<script>
import FlagsForm from "@/components/FlagsForm.vue";
import FlagsSubmit from "@/components/FlagsSubmit.vue";
import FlagsTable from "@/components/FlagsTable.vue";
import { mapActions } from "vuex";
import { flagsPerPage } from "@/config";
export default {
  components: { FlagsForm, FlagsSubmit, FlagsTable },
  data() {
    return { filtersOpen: false, manualOpen: false };
  },
  methods: mapActions(["fetchFlags"]),
  created: async function () {
    await this.fetchFlags({ page: 1, pageSize: flagsPerPage });
  },
};
</script>

<style scoped>
.flags-page {
  display: flex;
  flex-direction: column;
}

.flags-controls {
  flex: 0 0 auto;
  overflow: visible;
}

.compact-actions {
  display: none;
}

.flags-controls > .col {
  display: flex;
  flex-direction: column;
}

.flags-controls :deep(.q-card) {
  flex: 1;
}

.flags-list {
  display: flex;
  flex: 1 1 auto;
  flex-direction: column;
  min-height: 0;
  padding-top: 16px;
}

@media (min-width: 600px) and (max-width: 899px) {
  .flags-controls :deep(.q-card) {
    padding: 8px;
  }

  .flags-controls :deep(.q-card__section) {
    padding: 8px;
  }

  .flags-controls :deep(.q-pt-md) {
    padding-top: 8px;
  }
}

@media (max-width: 599px), (max-height: 929px) {
  .flags-controls {
    display: none;
  }

  .compact-actions {
    display: flex;
    flex: 0 0 auto;
    flex-wrap: wrap;
    gap: 12px;
  }
}
</style>
