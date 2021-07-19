<template>
  <v-container class="pa-1">
    <p class="subtitle-2 text--primary mt-0 mb-2">
      {{ title }}: {{ (totalAmount / 100.0) | humanizedCurrency }}
    </p>
    <v-expansion-panels flat :disabled="!hasEquities">
      <v-expansion-panel class="denseExpensionPanel">
        <v-expansion-panel-header class="px-0 pt-0">
          <investment-percentage
            :value="(1.0 * equityAmount) / totalAmount"
          ></investment-percentage>
        </v-expansion-panel-header>
        <v-expansion-panel-content class="denseExpensionPanelContent">
          <v-data-table
            calculate-widths
            :mobile-breakpoint="300"
            disable-sort
            disable-pagination
            hide-default-footer
            :items="overview.equities"
            :headers="equityHeaders"
          >
            <template v-slot:item.amount="{ item }">
              <span>{{ (item.currentValue / 100.0) | humanizedCurrency }}</span>
            </template>
            <template v-slot:item.change-percentage="{ item }">
              <equity-bar
                :min="0"
                :max="maxEquityChange * 1.2"
                :value="item.change"
              ></equity-bar>
            </template>
          </v-data-table>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>
</template>
<script>
module.exports = {
  props: ["title", "overview", "useCostBasis"],
  data: () => ({
    equityHeaders: [
      {
        text: "Name",
        align: "start",
        sortable: false,
        value: "name",
        width: "1%",
      },
      {
        text: "Amount",
        align: "end",
        sortable: true,
        value: "amount",
        width: "1%",
      },
      {
        text: "Change%",
        align: "center",
        sortable: true,
        value: "change-percentage",
      },
    ],
  }),
  computed: {
    equityAmount() {
      return this.useCostBasis
        ? this.overview.equityAmountByCostBasis
        : this.overview.equityAmount;
    },
    totalAmount() {
      return this.useCostBasis
        ? this.overview.totalAmountByCostBasis
        : this.overview.totalAmount;
    },
    hasEquities() {
      return (
        this.overview.equities !== null &&
        this.overview.equities !== undefined &&
        this.overview.equities.length > 0
      );
    },
    maxEquityChange() {
      if (!this.hasEquities) {
        return 1.0;
      }
      return Math.max(...this.overview.equities.map((x) => x.change));
    },
  },
  components: {
    "equity-bar": httpVueLoader("js/views/libs/equity-bar.vue"),
    "investment-percentage": httpVueLoader(
      "js/views/libs/investment-percentage.vue"
    ),
  },
  methods: {},
};
</script>
<style scoped>
.denseExpensionPanel > .v-expansion-panel-header {
  min-height: 24px;
  padding-bottom: 0px;
}
.denseExpensionPanelContent {
  padding-left: 0px;
  padding-right: 0px;
}
.denseExpensionPanelContent > .v-expansion-panel-content__wrap {
  padding-left: 0px;
  padding-right: 0px;
}
</style>