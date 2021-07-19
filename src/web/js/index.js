Vue.use(VueCurrencyFilter, {
  symbol: "$",
  thousandsSeparator: ",",
  fractionCount: 2,
  fractionSeparator: ".",
  symbolPosition: "front",
  symbolSpacing: false
});

Vue.directive("bubble", (el, binding, vnode) => {
  Object.keys(binding.modifiers).forEach(event => {
    // Bubble events of Vue components
    if (vnode.componentInstance) {
      vnode.componentInstance.$on(event, (...args) => {
        vnode.context.$emit(event, ...args);
      });

      // Bubble events of native DOM elements
    } else {
      el.addEventListener(event, payload => {
        vnode.context.$emit(event, payload);
      });
    }
  });
});

function formatDate(value) {
  if (value) {
    return moment(value).format("MMM Do, YYYY");
  } else {
    return "";
  }
}

function formatPercentage(value) {
  if (value === undefined || isNaN(value)) {
    return "-";
  }
  value *= 100;
  if (value < -10 || value > 10) {
    return value.toFixed(0) + "%";
  } else {
    return value.toFixed(1) + "%";
  }
}

function formatCurrency(value) {
  if (value === undefined || isNaN(value)) {
    return "-";
  }

  const sign = value < 0 ? "-" : "";
  value = Math.abs(value);
  if (value > 1000000) {
    return `${sign}$${(value / 1000000.0).toFixed(2)}M`;
  } else if (value > 100000) {
    return `${sign}$${(value / 1000.0).toFixed(0)}K`;
  } else if (value > 10000) {
    return `${sign}$${(value / 1000.0).toFixed(1)}K`;
  } else if (value > 1000) {
    return `${sign}$${(value / 1000.0).toFixed(2)}K`;
  } else {
    return `${sign}$${value.toFixed(2)}`;
  }
}

Vue.filter("date", formatDate);
Vue.filter("humanizedCurrency", formatCurrency);
Vue.filter("percentage", formatPercentage);

Vue.component(
  "currency-field",
  httpVueLoader("js/views/libs/currency-field.vue")
);

new Vue({
  el: "#app",
  data: {
    userId: null,
  },
  vuetify: new Vuetify(),
  router: new VueRouter({
    routes: ROUTES
  }),
  components: {},
  created: function () {
    firebase.initializeApp({
      apiKey: "AIzaSyAoPzACZK4PadNWZXyZ5LqV_gOERBEe9fY",
      projectId: "myfinance-7ca4a"
    });
    const auth = firebase.auth();
    auth.onAuthStateChanged(this.onAuthStateChanged);
    if (auth.currentUser) {
      this.onAuthStateChanged(auth.currentUser);
    }
  },
  methods: {
    onAuthStateChanged: function (user) {
      if (user) {
        if (user.uid != this.userId) {
          this.userId = user.uid;
        }
      } else {
        this.userId = null;
      }
    }
  }
});
