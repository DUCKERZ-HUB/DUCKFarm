<template>
  <q-table
    class="farm-bounded-table flags-table"
    :rows="flags"
    :columns="columns"
    :rows-per-page-options="[flagsPerPage]"
    v-model:pagination="pagination"
    @request="onRequest"
    row-key="flag"
    no-data-label="No flags for you"
    table-header-class="farm-table-header"
    :grid="$q.screen.lt.sm"
    dense
    wrap-cells
  >
    <template v-slot:top="scope">
      <div class="text-h6">{{ scope.pagination.rowsNumber }} flags total</div>
      <q-space />
      <pagination-custom
        :pagesNumber="scope.pagesNumber"
        :isFirstPage="scope.isFirstPage"
        :isLastPage="scope.isLastPage"
        :page="scope.pagination.page"
        :pageSize="scope.pagination.rowsPerPage"
        :total="scope.pagination.rowsNumber"
        @firstPage="scope.firstPage"
        @prevPage="scope.prevPage"
        @nextPage="scope.nextPage"
        @lastPage="scope.lastPage"
      />
      <q-btn
        flat
        round
        dense
        :icon="scope.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
        @click="scope.toggleFullscreen"
        class="q-ml-md"
      />
    </template>
    <template v-slot:no-data="{ message }">
      <div class="full-width row flex-center text-primary q-gutter-sm">
        <q-icon size="2em" name="sentiment_dissatisfied" />
        <span> Well this is sad... {{ message }} </span>
      </div>
    </template>
    <template v-slot:header-cell="props">
      <q-th :props="props" :class="'flag-col-' + props.col.name" :style="{ textAlign: 'center' }">
        {{ props.col.label }}
      </q-th>
    </template>
    <template v-slot:body-cell="props">
      <q-td :props="props" :class="'flag-col-' + props.col.name">
        <div class="flag-cell">
          <span class="flag-cell-value">{{ props.value }}</span>
          <q-btn
            size="sm"
            flat
            round
            icon="content_copy"
            v-if="copyableColumns.includes(props.col.name)"
            @click="copyToClipboard(props.value)"
          />
        </div>
      </q-td>
    </template>
    <template v-slot:item="props">
      <div class="col-12 q-pa-xs">
        <q-card class="q-pa-sm">
          <div v-for="col in props.cols" :key="col.name" class="flag-grid-row">
            <span class="flag-grid-label">{{ col.label }}</span>
            <span class="flag-grid-value">
              <span>{{ col.value || "-" }}</span>
              <q-btn
                v-if="copyableColumns.includes(col.name)"
                size="xs"
                flat
                round
                icon="content_copy"
                @click="copyToClipboard(col.value)"
              />
            </span>
          </div>
        </q-card>
      </div>
    </template>
    <template v-slot:pagination="scope">
      <pagination-custom
        :pagesNumber="scope.pagesNumber"
        :isFirstPage="scope.isFirstPage"
        :isLastPage="scope.isLastPage"
        :page="scope.pagination.page"
        :pageSize="scope.pagination.rowsPerPage"
        :total="scope.pagination.rowsNumber"
        @firstPage="scope.firstPage"
        @prevPage="scope.prevPage"
        @nextPage="scope.nextPage"
        @lastPage="scope.lastPage" /></template
  ></q-table>
</template>

<script>
import { mapState, mapActions } from "vuex";
import { copyToClipboard } from "quasar";
import moment from "moment";
import { flagsPerPage } from "@/config";
import PaginationCustom from "@/components/PaginationCustom.vue";

export default {
  components: { PaginationCustom },
  data: function () {
    return {
      columns: [
        { name: "sploit", label: "Sploit", field: "sploit", align: "center" },
        { name: "team", label: "Team", field: "team", align: "center" },
        { name: "flag", label: "Flag", field: "flag", align: "center" },
        {
          name: "time",
          label: "Time",
          field: "time",
          align: "center",
          format: (val) => moment.unix(val).format("YYYY-MM-DD HH:mm:ss"),
        },
        { name: "status", label: "Status", field: "status", align: "center" },
        {
          name: "checksystemResponse",
          label: "Checksystem response",
          field: "checksystemResponse",
          align: "left",
        },
      ],
      copyableColumns: ["sploit", "flag", "checksystemResponse"],
      flagsPerPage,
    };
  },
  computed: {
    pagination: {
      get: function () {
        return {
          page: this.selectedPage,
          rowsPerPage: flagsPerPage,
          rowsNumber: this.totalFlags,
        };
      },
      set: function (newPagination) {
        if (newPagination.page) {
          this.updatePage(newPagination.page);
        }
      },
    },
    ...mapState(["flags", "totalFlags", "selectedPage"]),
  },
  methods: {
    onRequest: async function (props) {
      this.pagination = props.pagination;
    },
    copyToClipboard,

    ...mapActions(["updatePage"]),
  },
};
</script>

<style scoped>
.flags-table :deep(.q-table) {
  width: 100%;
  table-layout: fixed;
}

.flags-table :deep(.q-table th),
.flags-table :deep(.q-table td) {
  padding: 4px 6px;
  white-space: normal;
  overflow-wrap: anywhere;
}

.flags-table :deep(.flag-col-sploit) { width: 14%; }
.flags-table :deep(.flag-col-team) { width: 7%; }
.flags-table :deep(.flag-col-flag) { width: 30%; }
.flags-table :deep(.flag-col-time) { width: 21%; }
.flags-table :deep(.flag-col-status) { width: 10%; }
.flags-table :deep(.flag-col-checksystemResponse) { width: 18%; }

.flag-cell {
  display: flex;
  align-items: center;
  gap: 2px;
}

.flag-cell-value {
  flex: 1 1 auto;
  min-width: 0;
  overflow-wrap: anywhere;
}

.flag-grid-row {
  display: flex;
  gap: 12px;
  padding: 4px 0;
}

.flag-grid-row + .flag-grid-row {
  border-top: 1px solid var(--farm-divider);
}

.flag-grid-label {
  flex: 0 0 105px;
  font-family: "Tilda Sans Bold", sans-serif;
}

.flag-grid-value {
  display: flex;
  flex: 1;
  align-items: flex-start;
  gap: 4px;
  min-width: 0;
  overflow-wrap: anywhere;
}

.flag-grid-value > span {
  min-width: 0;
}

.flags-table :deep(.q-table__grid-content) {
  min-height: 0;
  overflow-y: auto;
}
</style>
