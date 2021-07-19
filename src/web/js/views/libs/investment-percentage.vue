<template>
  <v-progress-linear height="25" reactive :value="100.0 * value">
    <template v-slot="{ value }">
      <strong style="color:white">{{ value/100.0 | percentage }} invested</strong>
    </template>
  </v-progress-linear>
</template>
<script>
module.exports = {
  props: ["value"],
  data: () => ({})
};
</script>