<template>
  <q-card class="q-pa-md">
    <q-card-section>
      <div class="text-h6">Filter flags</div>
    </q-card-section>
    <q-card-section>
      <q-form class="flags-filter-form" @submit.prevent="onSubmit">
        <div class="row">
          <div class="col-12 col-sm-4 q-px-sm q-pb-sm">
            <q-select
              dense
              outlined
              v-model="sploit"
              :options="sploitOptions"
              aria-label="Sploit"
              :display-value="sploit || 'Sploit'"
              :class="{ 'empty-select': !sploit }"
              ><template v-if="sploit" v-slot:append>
                <q-icon
                  name="close"
                  size="18px"
                  color="primary"
                  @click.stop="sploit = null"
                  class="cursor-pointer"
                /> </template
            ></q-select>
          </div>
          <div class="col-12 col-sm-4 q-px-sm q-pb-sm">
            <q-select
              dense
              outlined
              v-model="team"
              :options="teamOptions"
              aria-label="Team"
              :display-value="team || 'Team'"
              :class="{ 'empty-select': !team }"
              ><template v-if="team" v-slot:append>
                <q-icon
                  name="close"
                  size="18px"
                  color="primary"
                  @click.stop="team = null"
                  class="cursor-pointer"
                /> </template
            ></q-select>
          </div>
          <div class="col-12 col-sm-4 q-px-sm q-pb-sm">
            <q-input
              dense
              outlined
              v-model="flag"
              aria-label="Flag"
              placeholder="Flag"
              hint="substring, case-insensitive"
              ><template v-if="flag" v-slot:append>
                <q-icon
                  name="close"
                  size="18px"
                  color="primary"
                  @click.stop="flag = null"
                  class="cursor-pointer"
                /> </template
            ></q-input>
          </div>
        </div>
        <div class="row q-pt-md">
          <div class="col-12 col-sm-6 col-md-3 q-px-sm q-pb-sm">
            <q-input
              dense
              outlined
              v-model="since"
              aria-label="Since"
              placeholder="Since"
              :hint="'yyyy-mm-dd hh:mm (' + (serverTZ || 'UTC') + ')'"
              ><template v-if="since" v-slot:append>
                <q-icon
                  name="close"
                  size="18px"
                  color="primary"
                  @click.stop="since = null"
                  class="cursor-pointer"
                /> </template
            ></q-input>
          </div>
          <div class="col-12 col-sm-6 col-md-3 q-px-sm q-pb-sm">
            <q-input
              dense
              outlined
              v-model="until"
              aria-label="Until"
              placeholder="Until"
              :hint="'yyyy-mm-dd hh:mm (' + (serverTZ || 'UTC') + ')'"
              ><template v-if="until" v-slot:append>
                <q-icon
                  name="close"
                  size="18px"
                  color="primary"
                  @click.stop="until = null"
                  class="cursor-pointer"
                /> </template
            ></q-input>
          </div>
          <div class="col-12 col-sm-6 col-md-2 q-px-sm q-pb-sm">
            <q-select
              dense
              outlined
              v-model="status"
              :options="statusOptions"
              aria-label="Status"
              :display-value="status || 'Status'"
              :class="{ 'empty-select': !status }"
              ><template v-if="status" v-slot:append>
                <q-icon
                  name="close"
                  size="18px"
                  color="primary"
                  @click.stop="status = null"
                  class="cursor-pointer"
                /> </template
            ></q-select>
          </div>
          <div class="col-12 col-sm-6 col-md-4 q-px-sm q-pb-sm">
            <q-input
              dense
              outlined
              v-model="checksystemResponse"
              aria-label="Checksystem response"
              placeholder="Checksystem response"
              hint="substring, case-insensitive"
              ><template v-if="checksystemResponse" v-slot:append>
                <q-icon
                  name="close"
                  size="18px"
                  color="primary"
                  @click.stop="checksystemResponse = null"
                  class="cursor-pointer"
                /> </template
            ></q-input>
          </div>
        </div>
        <div class="q-pt-md">
          <q-btn label="Filter" type="submit" color="primary" />
        </div>
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
import { mapState, mapActions, mapMutations } from "vuex";

export default {
  data: function () {
    return {
      sploit: null,

      team: null,

      flag: null,
      since: null,
      until: null,

      status: null,

      checksystemResponse: null,
    };
  },
  methods: {
    onSubmit: async function () {
      const filters = {
        sploit: this.sploit,
        team: this.team,
        flag: this.flag,
        since: this.since,
        until: this.until,
        status: this.status,
        checksystem_response: this.checksystemResponse,
      };

      this.setFlagFilters(filters);
      this.setSelectedPage(1);
      await this.fetchFlags();
    },
    ...mapActions(["fetchFlags"]),
    ...mapMutations(["setSelectedPage", "setFlagFilters"]),
  },
  computed: mapState({
    sploitOptions: "sploitFilterOptions",
    teamOptions: "teamFilterOptions",
    statusOptions: "statusFilterOptions",
    serverTZ: "serverTZ",
  }),
};
</script>

<style></style>
