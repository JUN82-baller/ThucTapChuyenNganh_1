<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-[#1f1f1f]">
    <div class="bg-[#181818] p-8 rounded-lg shadow-lg w-80">
      <h2 class="text-2xl font-bold text-white mb-6 text-center">Login</h2>

      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label class="block text-gray-300 mb-2" for="username">Username</label>
          <input
            v-model="username"
            id="username"
            type="text"
            placeholder="Enter your username"
            class="w-full px-3 py-2 rounded bg-gray-800 text-white focus:outline-none"
          />
        </div>

        <div class="mb-6">
          <label class="block text-gray-300 mb-2" for="password">Password</label>
          <input
            v-model="password"
            id="password"
            type="password"
            placeholder="Enter your password"
            class="w-full px-3 py-2 rounded bg-gray-800 text-white focus:outline-none"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded mb-4"
        >
          Login
        </button>

        <button
          type="button"
          @click="loginWithGoogle"
          class="w-full bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded flex items-center justify-center mb-3"
        >
          <img
            src="https://www.svgrepo.com/show/475656/google-color.svg"
            alt="Google"
            class="w-5 h-5 mr-2"
          />
          Continue with Google
        </button>

        <button
          type="button"
          @click="loginWithFacebook"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded flex items-center justify-center"
        >
          <img
            src="https://www.svgrepo.com/show/452196/facebook-1.svg"
            alt="Facebook"
            class="w-5 h-5 mr-2"
          />
          Continue with Facebook
        </button>
      </form>

      <div class="mt-4 text-green-400 text-center" v-if="loginSuccess">Login successful!</div>

      <p class="mt-4 text-gray-400 text-center">
        Don't have an account?
        <span @click="goToRegister" class="text-green-500 hover:underline cursor-pointer">Register here</span>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const loginSuccess = ref(false);
const router = useRouter();

function handleLogin() {
  if (username.value && password.value) {
    loginSuccess.value = true;
    setTimeout(() => {
      router.push("/");
    }, 1000);
  } else {
    loginSuccess.value = false;
    alert("Please enter both username and password.");
  }
}

function loginWithGoogle() {
  alert("Google login clicked!");
}

function loginWithFacebook() {
  alert("Facebook login clicked!");
}

function goToRegister() {
  router.push("/register");
}
</script>

<style scoped>
input::placeholder {
  color: #aaa;
}
</style>
