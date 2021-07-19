<template>
  <div class="equityBarContainer">
    <div class="referenceLine" :style="{width: referenceWidth}"></div>
    <div class="equityBar">
      <div
        :class="value > 1.0 ? 'positivePosition' : 'negativePosition'"
        :style="{width: currentPositionWidth}"
      >
        <span class="text">{{ displayValue }}</span>
      </div>
    </div>
  </div>
</template>
<script>
module.exports = {
  props: ["min", "max", "value"],
  computed: {
    normalizedMin() {
      return Math.min(this.min, 0.9);
    },
    normalizedMax() {
      return Math.max(this.max, 1.1);
    },
    referenceWidth() {
      return (
        (100 * (1.0 - this.normalizedMin)) /
          (this.normalizedMax - this.normalizedMin) +
        "%"
      );
    },
    currentPositionWidth() {
      return (
        (100 * (this.value - this.normalizedMin)) /
          (this.normalizedMax - this.normalizedMin) +
        "%"
      );
    },
    displayValue() {
      return ((this.value - 1) * 100).toFixed(0) + "%";
    }
  },
  methods: {}
};
</script>
<style scoped>
.equityBarContainer {
  position: relative;
  height: 2em;
}
.referenceLine {
  position: absolute;
  border-right: solid 2px #aaa;
  height: 1.7em;
  z-index: 2;
  margin-top: 0.15em;
}
.equityBar {
  position: absolute;
  background-color: #e7e7e7;
  height: 1.2em;
  width: 100%;
  margin-top: 0.4em;
}
.positivePosition,
.negativePosition {
  height: 1.2em;
  position: absolute;
  padding-right: 5px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.positivePosition {
  background-color: #2e7d32;
  color: white;
}
.negativePosition {
  background-color: #c62828;
  color: white;
}
.text {
  z-index: 3;
}
</style>