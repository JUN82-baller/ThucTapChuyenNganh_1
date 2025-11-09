<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-[#1f1f1f]">
    <div class="bg-[#181818] p-8 rounded-lg shadow-lg w-90">
      <h2 class="text-2xl font-bold text-white mb-6 text-center">Register</h2>

      <form @submit.prevent="handleRegister">
        <div class="mb-4">
          <label class="block text-gray-300 mb-2" for="username">Username</label>
          <input
            v-model="username"
            id="username"
            type="text"
            placeholder="Choose a username"
            class="w-full px-3 py-2 rounded bg-gray-800 text-white focus:outline-none"
          />
        </div>

        <div class="mb-4">
          <label class="block text-gray-300 mb-2" for="email">Email</label>
          <input
            v-model="email"
            id="email"
            type="email"
            placeholder="Enter your email"
            class="w-full px-3 py-2 rounded bg-gray-800 text-white focus:outline-none"
          />
        </div>

        <div class="mb-4">
          <label class="block text-gray-300 mb-2" for="password">Password</label>
          <input
            v-model="password"
            id="password"
            type="password"
            placeholder="Create a password"
            class="w-full px-3 py-2 rounded bg-gray-800 text-white focus:outline-none"
          />
        </div>

        <div class="mb-6">
          <label class="block text-gray-300 mb-2" for="confirmPassword">Confirm Password</label>
          <input
            v-model="confirmPassword"
            id="confirmPassword"
            type="password"
            placeholder="Confirm your password"
            class="w-full px-3 py-2 rounded bg-gray-800 text-white focus:outline-none"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded mb-4"
        >
          Register
        </button>

        <button
          type="button"
          @click="registerWithGoogle"
          class="w-full bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded flex items-center justify-center mb-3"
        >
          <img
            src="https://www.svgrepo.com/show/475656/google-color.svg"
            alt="Google"
            class="w-5 h-5 mr-2"
          />
          Sign up with Google
        </button>

        <button
          type="button"
          @click="registerWithFacebook"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded flex items-center justify-center"
        >
          <img
            src="https://www.svgrepo.com/show/452196/facebook-1.svg"
            alt="Facebook"
            class="w-5 h-5 mr-2"
          />
          Sign up with Facebook
        </button>
      </form>

      <div v-if="registerSuccess" class="mt-4 text-green-400 text-center">
        Registration successful! Redirecting...
      </div>

      <p class="mt-4 text-gray-400 text-center">
        Already have an account?
        <span @click="goToLogin" class="text-green-500 hover:underline cursor-pointer"
          >Login here</span
        >
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const username = ref("");
const email = ref("");
const password = ref("");
const confirmPassword = ref("");
const registerSuccess = ref(false);
const router = useRouter();

function handleRegister() {
  if (!username.value || !email.value || !password.value || !confirmPassword.value) {
    alert("Please fill in all fields.");
    return;
  }

  if (password.value !== confirmPassword.value) {
    alert("Passwords do not match.");
    return;
  }

  registerSuccess.value = true;
  setTimeout(() => {
    router.push("/login");
  }, 1000);
}

function registerWithGoogle() {
  alert("Google sign-up clicked!");
}

function registerWithFacebook() {
  alert("Facebook sign-up clicked!");
}

function goToLogin() {
  router.push("/login");
}
</script>

<style scoped>
input::placeholder {
  color: #aaa;
}
</style>
