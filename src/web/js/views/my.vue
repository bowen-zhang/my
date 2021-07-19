<template>
  <v-container pa-0>
    <v-navigation-drawer v-model="drawer" app>
      <v-list dense>
        <v-list-item>
          <v-avatar color="blue" class="mb-2">
            <span class="white--text subtitle-1">{{ userInitals }}</span>
          </v-avatar>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item link :to="{ path: '/my/dashboard' }">
          <v-list-item-action>
            <v-icon>mdi-finance</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </p>My Next Idea</p>
    </v-app-bar>
    <v-main>
      <v-breadcrumbs :items="navigationPaths" class="py-3">
        <template v-slot:divider>
          <v-icon>mdi-chevron-right</v-icon>
        </template>
      </v-breadcrumbs>
      <router-view></router-view>
    </v-main>
  </v-container>
</template>
<script>
module.exports = {
  props: ["userId"],
  data: function () {
    return {
      drawer: false,
    };
  },
  components: {},
  created: function () {},
  watch: {
    userId: function (newVal) {},
    $route: function (val) {},
  },
  computed: {
    userInitals() {
      function _firstChar(str) {
        return str.length > 0 ? str[0].toUpperCase() : "";
      }
      if (this.user) {
        return _firstChar(this.user.firstName) + _firstChar(this.user.lastName);
      } else {
        return "?";
      }
    },
    navigationPaths: function () {
      const segments = this.$route.path.split("/").filter((x) => x.length > 0);
      const items = [];
      var path = "";
      for (var i = 0; i < segments.length; ++i) {
        path += "/" + segments[i];
        items.push({
          text: segments[i],
          disabled: i == 0 || i == segments.length - 1,
          exact: true,
          to: path,
        });
      }
      return items;
    },
  },
  methods: {},
};
</script>
<style scoped>
</style>