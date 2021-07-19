<template>
  <v-dialog ref="dialog" v-model="modal" width="80%">
    <template v-slot:activator="{ on }">
      <v-text-field hide-details dense :value="dateString" :label="label" readonly v-on="on"></v-text-field>
    </template>
    <v-date-picker :value="dateValue" scrollable no-title @change="onChange"></v-date-picker>
  </v-dialog>
</template>
<script>
module.exports = {
  props: ["label", "value"],
  data: () => ({
    modal: false
  }),
  computed: {
    dateString() {
      if (this.value) {
        return moment(this.value).format("MMM Do, YYYY");
      } else {
        return "";
      }
    },
    dateValue() {
      if (this.value) {
        return this.value.toISOString().substr(0, 10);
      } else {
        return "";
      }
    }
  },
  methods: {
    onChange: function(newDateValue) {
      this.$emit("update:value", new Date(newDateValue));
      this.modal = false;
    }
  }
};
</script>
<style scoped>
</style>