<template>
  <q-page class="q-pa-md farm-page farm-list-page">
    <teams-table />
  </q-page>
</template>

<script>
import TeamsTable from "@/components/TeamsTable.vue";
import { mapActions } from "vuex";
export default {
  components: { TeamsTable },
  created: async function () {
    await this.fetchTeams();
  },
  methods: mapActions(["fetchTeams"]),
};
</script>

<style></style>
