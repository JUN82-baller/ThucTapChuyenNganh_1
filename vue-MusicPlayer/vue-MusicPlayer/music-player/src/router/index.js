import { createRouter, createWebHistory } from "vue-router";

import MainLayout from "@/layouts/MainLayout.vue";
import AuthLayout from "@/layouts/AuthLayout.vue";

import HomeView from "@/views/HomeView.vue";
import SearchView from "@/views/SearchView.vue";
import LibraryView from "@/views/LibraryView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Main App Layout
    {
      path: "/",
      component: MainLayout,
      children: [
        { path: "", name: "home", component: HomeView },
        { path: "search", name: "search", component: SearchView },
        { path: "library", name: "library", component: LibraryView },
      ],
    },

    // Auth Layout
    {
      path: "/",
      component: AuthLayout,
      children: [
        { path: "login", name: "login", component: LoginView },
        { path: "register", name: "register", component: RegisterView },
      ],
    },
  ],
});

export default router;
