<template>
  <v-dialog v-model="dialog" max-width="90%" style="{ zIndex: 200 }" @keydown.esc="cancel">
    <v-card>
      <v-card-title>{{ text }}</v-card-title>
      <v-card-actions class="pt-0">
        <v-spacer></v-spacer>
        <v-btn color="primary darken-1" text @click.native="agree">{{ okText }}</v-btn>
        <v-btn color="grey" text @click.native="cancel">{{ cancelText }}</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
module.exports = {
  data: () => ({
    dialog: false,
    text: "",
    okText: "",
    cancelText: "",
    resolve: null,
    reject: null
  }),
  methods: {
    open(text, okText = "Yes", cancelText = "No") {
      this.text = text;
      this.okText = okText;
      this.cancelText = cancelText;
      this.dialog = true;
      return new Promise((resolve, reject) => {
        this.resolve = resolve;
        this.reject = reject;
      });
    },
    agree() {
      this.dialog = false;
      this.resolve();
    },
    cancel() {
      this.dialog = false;
      this.reject();
    }
  }
};
</script>