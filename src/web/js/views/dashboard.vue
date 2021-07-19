<template>
  <v-container>
    <div id="chart"></div>
  </v-container>
</template>
<script>
module.exports = {
  props: [],
  data: function () {
    return {
      chart: null,
    };
  },
  computed: {},
  components: {},
  watch: {},
  created: function () {
    google.charts.load("current", { packages: ["corechart", "line"] });
    google.charts.setOnLoadCallback(() => {
      this.chart = new google.visualization.LineChart(
        document.getElementById("chart")
      );
      this.refresh();
    });
  },
  methods: {
    refresh: function () {
      var client = new proto.my.MyServiceClient("http://192.168.86.250:8082");

      var request = new proto.my.TestRequest();
      request.setCount(10);

      client.test(request, {}, (err, response) => {
        window.r = response;
        var data = new google.visualization.DataTable();
        data.addColumn("number", "X");
        data.addColumn("number", "Dogs");

        data.addRows(response.getDataList().map((d) => [d.getX(), d.getY()]));

        var options = {
          hAxis: {
            title: "Time",
          },
          vAxis: {
            title: "Popularity",
          },
        };

        this.chart.draw(data, options);
      });
    },
  },
};
</script>
<style scoped>
</style>