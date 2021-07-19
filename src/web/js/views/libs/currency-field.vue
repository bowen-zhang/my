<template>
  <v-text-field
    ref="field"
    hide-details
    dense
    :readonly="readonly"
    :label="label"
    :value="displayValue"
    prefix="$"
    @change="onChange"
    v-bubble.focus.blur.keyup
  ></v-text-field>
</template>
<script>
module.exports = {
  props: ["label", "value", "readonly"],
  computed: {
    displayValue() {
      return (this.value / 100.0).toFixed(2);
    }
  },
  methods: {
    onChange(newValue) {
      this.$emit("update:value", parseInt(newValue * 100));
    },
    focus() {
      this.$refs.field.focus();
    }
  }
};
</script>