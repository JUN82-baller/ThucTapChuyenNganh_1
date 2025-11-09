<script setup>
import { onMounted } from "vue";
import { RouterLink, RouterView } from "vue-router";
import MenuItem from "@/components/MenuItem.vue";
import MusicPlayer from "@/components/MusicPlayer.vue";
import { useSongStore } from "@/stores/song";
import { storeToRefs } from "pinia";

const useSong = useSongStore();
const { isPlaying, currentTrack } = storeToRefs(useSong);

onMounted(() => {
  isPlaying.value = false;
});
</script>

<template>
  <!-- Top Navigation -->
  <div
    id="TopNav"
    class="w-[calc(100%-230px)] h-[60px] fixed right-0 z-20 bg-[#101010] bg-opacity-80 flex items-center justify-end"
  >
    <RouterLink to="/login" class="text-gray-400 hover:text-white">Login</RouterLink>
    <div class="px-2 text-gray-400">/</div>
    <RouterLink to="/register" class="text-gray-400 hover:text-white mr-0.5">Register</RouterLink>
  </div>

  <!-- Side Navigation -->
  <div id="SideNav" class="h-[100%] p-6 w-[230px] fixed z-50 bg-black">
    <RouterLink to="/">
      <img width="180" src="/images/icons/weemusic.png" alt="logo" class="px-1.5" />
    </RouterLink>
    <div class="my-8"></div>
    <ul>
      <RouterLink to="/">
        <MenuItem name="Home" iconString="home" pageUrl="/" />
      </RouterLink>
      <RouterLink to="/search">
        <MenuItem name="Search" iconString="search" pageUrl="/search" />
      </RouterLink>
      <RouterLink to="/library">
        <MenuItem name="Your Library" iconString="library" pageUrl="/library" />
      </RouterLink>
      <div class="py-3.5"></div>
      <MenuItem name="Create Playlist" iconString="playlist" pageUrl="/playlist" />
      <MenuItem name="Liked Songs" iconString="liked" pageUrl="/liked" />
    </ul>
  </div>

  <!-- Main Content -->
  <div
    class="fixed right-0 top-0 w-[calc(100%-230px)] overflow-auto h-full bg-gradient-to-b from-[#1C1C1C] to-black"
  >
    <div class="mt-[70px]"></div>
    <RouterView />
    <div class="mb-[100px]"></div>
  </div>

  <MusicPlayer v-if="currentTrack" />
</template>
