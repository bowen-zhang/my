<template>
  <v-chip class="editable-chip" :close="!readonly" color="grey lighten-2" @click:close="onClose">
    <div class="label">{{ label }}</div>
    <div class="relationship">{{ relationship }}</div>
    <div class="display" v-show="!edit" @click="toEdit">{{ displayValue }}</div>
    <div class="editor" v-show="edit">
      <v-text-field
        v-if="type==='text'"
        ref="field"
        dense
        hide-details
        :value="value"
        @input="onInput"
        @focus="onFocus"
        @keyup.enter="startEdit"
        @blur="stopEdit"
        class="mt-0"
      ></v-text-field>
      <currency-field
        v-if="type==='currency'"
        ref="field"
        :value="value"
        @input="onInput"
        @focus="onFocus"
        @keyup.enter="startEdit"
        @blur="stopEdit"
        class="mt-0"
      ></currency-field>
      <v-select
        v-if="type==='select'"
        ref="field"
        :value="value"
        @input="onInput"
        @blur="stopEdit"
        :items="this.items"
        :item-text="this.itemText"
        :item-value="this.itemValue"
        dense
      ></v-select>
    </div>
  </v-chip>
</template>
<script>
module.exports = {
  props: [
    "type",
    "label",
    "relationship",
    "value",
    "items",
    "itemText",
    "itemValue",
    "readonly"
  ],
  data: () => ({
    edit: false
  }),
  computed: {
    displayValue() {
      if (this.type === "text") {
        return `"${this.value}"`;
      } else if (this.type === "currency") {
        return formatCurrency((this.value / 100.0).toFixed(2));
      } else if (this.type === "select") {
        const item = this.items.find(x => x[this.itemValue] === this.value);
        return item ? item[this.itemText] : null;
      } else {
        return null;
      }
    }
  },
  methods: {
    toEdit() {
      if (this.readonly) {
        return;
      }
      this.edit = true;
      this.$nextTick(() => {
        this.$refs.field.focus();
      });
    },
    onFocus(event) {
      event.target.select();
    },
    stopEdit() {
      this.edit = false;
    },
    startEdit() {
      this.edit = false;
    },
    onInput(val) {
      this.$emit("update:value", val);
    },
    onClose() {
      this.$emit("close");
    }
  }
};
</script>
<style scoped>
.editable-chip {
  margin: 1px 1px 1px 1px;
}

.relationship {
  padding-right: 4px;
  padding-left: 6px;
  color: #777;
}

.display {
  padding: 3px 4px 3px 4px;
  border: solid 1px transparent;
  max-width: 200px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.display:hover {
  border: solid 1px #999;
}

.editor .v-text-field {
  width: 100px;
  font-size: inherit;
}
.editor .v-text-field input {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
}
.editor .v-select {
  max-width: 200px;
  font-size: inherit;
}
.editor .v-select .v-input__slot {
  margin-bottom: 0px;
}
.editor .v-select .v-select__selection {
  margin-top: 10px;
  margin-bottom: 0px;
}

.close {
  transform: scale(0.7);
}
</style>