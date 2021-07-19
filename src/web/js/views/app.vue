<template>
  <v-container pa-0>
    <div id="firebaseui-auth-container"></div>
    <v-navigation-drawer app v-model="drawer">
      <v-list dense>
        <v-list-item link :to="{ path: '/app/signin' }">
          <v-list-item-action>
            <v-icon>mdi-login-variant</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Sign In</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link :to="{ path: '/app/signup' }">
          <v-list-item-action>
            <v-icon>mdi-account-plus</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Sign Up</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link :to="{ path: 'app/pricing' }">
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Pricing</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-btn v-if="userId === null" :to="{ path: '/app/signin' }" rounded
        >Sign In</v-btn
      >
    </v-app-bar>
    <v-main>
      <router-view :user-id="userId"></router-view>
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
    userId: function (newVal) {
      if (newVal) {
        this.$router.push({ path: "/my" });
      } else {
        this.$router.push({ path: "/app" });
      }
    },
  },
  methods: {},
};
</script>
<style scoped>
</style>