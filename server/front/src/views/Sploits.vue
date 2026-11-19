<template>
  <q-page class="q-pa-md farm-page farm-list-page">
    <div v-if="error" class="text-negative q-mb-md" role="alert">
      Could not load sploits: {{ error }}
    </div>
    <q-table
      class="farm-bounded-table sploits-table"
      dense
      v-model:pagination="pagination"
      :rows="sploits"
      :columns="columns"
      :loading="loading"
      :rows-per-page-options="[0]"
      row-key="name"
      no-data-label="No sploits registered yet"
      table-header-class="bg-primary text-white"
    >
      <template v-slot:body-cell-description="props">
        <q-td :props="props">
          <div class="sploit-description">{{ props.value || "-" }}</div>
        </q-td>
      </template>
      <template v-slot:no-data="{ message }">
        <div class="full-width row flex-center text-primary q-gutter-sm">
          <q-icon size="2em" name="sentiment_dissatisfied" />
          <span> Well this is sad... {{ message }} </span>
        </div>
      </template>
    </q-table>
  </q-page>
</template>

<script>
import APIService from "@/services/api";

export default {
  name: "SploitsView",
  data() {
    return {
      sploits: [],
      loading: false,
      error: null,
      refreshTimer: null,
      pagination: { sortBy: "accepted_last_10m", descending: true, rowsPerPage: 0 },
      columns: [
        { name: "name", label: "Sploit", field: "name", align: "left", sortable: true },
        {
          name: "description",
          label: "Description",
          field: "description",
          align: "left",
          sortable: true,
        },
        {
          name: "received_total",
          label: "Received total",
          field: "received_total",
          align: "right",
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "received_last_10m",
          label: "Received 10 min",
          field: "received_last_10m",
          align: "right",
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "accepted_total",
          label: "Accepted total",
          field: "accepted_total",
          align: "right",
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "accepted_last_10m",
          label: "Accepted 10 min",
          field: "accepted_last_10m",
          align: "right",
          sortable: true,
          sort: (a, b) => a - b,
        },
      ],
    };
  },
  mounted() {
    this.fetchSploits();
    this.refreshTimer = window.setInterval(() => this.fetchSploits(), 30000);
  },
  beforeUnmount() {
    window.clearInterval(this.refreshTimer);
  },
  methods: {
    async fetchSploits() {
      this.loading = true;
      try {
        const { data } = await APIService.get("/sploits");
        this.sploits = data;
        this.error = null;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.sploit-description {
  min-width: 260px;
  max-width: 520px;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.sploits-table :deep(.q-table tbody tr) {
  height: 39px;
}
</style>
