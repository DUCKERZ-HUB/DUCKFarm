<template>
  <q-page class="q-pa-md farm-page flags-page">
    <div class="row justify-between q-col-gutter-md flags-controls">
      <div class="col col-12 col-md-8"><flags-form /></div>
      <div class="col col-12 col-md-4"><flags-submit /></div>
    </div>
    <div class="flags-list">
      <flags-table />
    </div>
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
  max-height: 60%;
  overflow-y: auto;
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
</style>
