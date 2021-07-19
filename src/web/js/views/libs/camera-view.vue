<template>
  <v-container ma-0 pa-0>
    <v-row v-show="!captured">
      <v-col cols="12" class="text-center">
        <video ref="video" width="100%" autoplay></video>
        <v-btn fab small relative color="primary" style="bottom:22px" @click="capture">
          <v-icon>mdi-camera</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-row v-show="captured">
      <v-col cols="12">
        <img ref="snapshot" width="100%"></img>
      </v-col>
    </v-row>
    <canvas v-show="false" ref="canvas" :width="width" :height="height" style="border: solid 1px red"></canvas>
  </v-container>
</template>
<script>
module.exports = {
  data: () => ({
    stream: null,
    width: null,
    height: null,
    captured: false
  }),
  computed: {
    msg: function() {
      return navigator.mediaDevices;
    }
  },
  mounted() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        this.stream = stream;
        const settings = stream.getTracks()[0].getSettings();
        this.width = settings.width;
        this.height = settings.height;
        this.$refs.video.srcObject = stream;
        this.$refs.video.play();
      });
    }
  },
  beforeDestroy() {
    this.stream.getTracks().forEach(track => track.stop());
  },
  methods: {
    capture: function() {
      const context = this.$refs.canvas.getContext("2d");
      context.drawImage(this.$refs.video, 0, 0, this.width, this.height);
      const dataUri = this.$refs.canvas.toDataURL('image/jpeg')
      this.$refs.snapshot.src = dataUri;
      this.captured = true;
    }
  }
};
</script>