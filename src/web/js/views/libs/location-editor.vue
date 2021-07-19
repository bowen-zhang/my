<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-text-field label="Address" v-model="location.address" hide-details dense></v-text-field>
      </v-col>
      <v-col cols="5">
        <v-text-field label="City" v-model="location.city" hide-details dense></v-text-field>
      </v-col>
      <v-col cols="3">
        <v-text-field label="State" v-model="location.state" hide-details dense></v-text-field>
      </v-col>
      <v-col cols="4">
        <v-text-field label="Zipcode" v-model="location.zipcode" hide-details dense></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
module.exports = {
  props: ["location"],
  data: function() {
    return {};
  },
  created: function() {},
  methods: {}
};
</script>
<style scoped>
</style>