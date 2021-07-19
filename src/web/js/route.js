const ROUTES = [
  {
    path: "/",
    redirect: "/app"
  },
  {
    path: "/app",
    component: httpVueLoader("js/views/app.vue"),
    children: [
      { path: "", redirect: "/app/cover" },
      { path: "cover", component: httpVueLoader("js/views/cover.vue") },
      { path: "signin", component: httpVueLoader("js/views/signin.vue") }
    ]
  },
  {
    path: "/my",
    component: httpVueLoader("js/views/my.vue"),
    children: [
      { path: "", redirect: "/my/dashboard" },
      { path: "dashboard", component: httpVueLoader("js/views/dashboard.vue") },
      { path: "settings", component: httpVueLoader("js/views/settings.vue") },
    ]
  }
];
