<template>
  <v-container>
    <div id="firebaseui-auth-container"></div>
  </v-container>
</template>
<script>
module.exports = {
  props: ["userId"],
  data: function() {
    return {};
  },
  created: function() {
    const ui = new firebaseui.auth.AuthUI(firebase.auth());
    ui.start("#firebaseui-auth-container", {
      callbacks: {
        signInSuccessWithAuthResult: this.onSignInSuccess
      },
      signInFlow: "popup",
      signInOptions: [firebase.auth.EmailAuthProvider.PROVIDER_ID]
    });
  },
  methods: {
    onSignInSuccess: function(authResult, redirectUrl) {
      return false;
    }
  }
};
</script>
<style scoped>
</style>