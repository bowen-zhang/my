<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="title">Family Sharing</v-col>
    </v-row>
    <v-row v-if="isLoadingFamily">
      <v-col cols="12" class="text-center">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
      </v-col>
    </v-row>
    <v-row v-if="hasNoFamily">
      <v-col cols="8">
        <v-text-field placeholder="Family Name" v-model="family.name" hide-details dense></v-text-field>
      </v-col>
      <v-col cols="4">
        <v-btn color="primary" @click="createFamily">Create</v-btn>
    </v-row>
    <v-row v-if="isInvitedToFamily">
      <v-col cols="12">
        You are invited to join "{{ family.name }}".
      </v-col>
      <v-col cols="12" class="d-flex justify-space-around">
        <v-btn color="green" class="white--text" @click="joinFamily">Accept</v-btn>
        <v-btn color="red" class="white--text" @click="leaveFamily">Decline</v-btn>
      </v-col>
    </v-row>
    <v-row v-if="hasJoinedFamily">
      <v-col cols="12">
        <p class="text-center">{{ family.name }}</p>
        <v-container>
          <v-row>
            <v-col cols="4" v-for="member in family.members" :key="member.userId" class="text-center">
              <v-badge v-if="member.accepted" icon="mdi-check-bold" color="green" avatar bordered overlap>
                <v-avatar>
                  <v-icon x-large>mdi-account-circle</v-icon>
                </v-avatar>
              </v-badge>
              <v-badge v-else icon="mdi-help" color="orange" avatar bordered overlap>
                <v-avatar>
                  <v-icon x-large>mdi-account-circle</v-icon>
                </v-avatar>
              </v-badge>
              <div>{{ member.firstName }} {{ member.lastName }}</div>
            </v-col>
          </v-row>
        </v-container>
      </v-col>
      <v-col cols="8">
        <v-text-field placeholder="Family member email" v-model="newMemberEmail" hide-details dense></v-text-field>
      </v-col>
      <v-col cols="4">
        <v-btn color="primary" @click="invite">Invite</v-btn>
      </v-col>
      <v-col cols="12" class="text-center">
        <v-btn color="red" @click="leaveFamily">Leave</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
module.exports = {
  props: ["api"],
  data: function () {
    return {
      family: null,
      newMemberEmail: "",
    };
  },
  computed: {},
  components: {},
  watch: {
    api: function (newVal) {
      if (newVal) {
        this.load();
      }
    },
  },
  created: function () {
    if (this.api) {
      this.load();
    }
  },
  computed: {
    isLoadingFamily() {
      return !this.family;
    },
    hasNoFamily() {
      return this.family && !this.family.id;
    },
    isInvitedToFamily() {
      return (
        this.family &&
        this.family.id &&
        this.family.members.find(
          (m) => m.userId == this.api.getUserId() && !m.accepted
        )
      );
    },
    hasJoinedFamily() {
      return (
        this.family &&
        this.family.id &&
        this.family.members.find(
          (m) => m.userId == this.api.getUserId() && m.accepted
        )
      );
    },
  },
  methods: {
    load() {
      this.api.families.getByUser((family) => {
        if (family) {
          this.family = family;
        } else {
          this.family = { name: "" };
        }
      });
    },
    createFamily() {
      this.api.families.create(this.newFamilyName, (family) => {
        this.family = family;
      });
    },
    invite() {
      this.api.inviteToFamily(
        this.family.id,
        this.newMemberEmail,
        (message) => {
          console.log(message);
          this.newMemberEmail = "";
          this.load();
        }
      );
    },
    joinFamily() {
      this.api.families.join(this.family.id, (response) => {
        this.load();
      });
    },
    leaveFamily() {
      this.api.families.leave(this.family.id, (response) => {
        this.load();
      });
    },
    getStatusText(member) {
      if (member.accepted) {
        return "Accepted";
      } else {
        return "Pending";
      }
    },
  },
};
</script>
<style scoped>
</style>