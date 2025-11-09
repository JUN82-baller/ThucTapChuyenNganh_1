<script setup>
import { onMounted, computed } from 'vue'
import SongRow from '../components/SongRow.vue'
import Play from 'vue-material-design-icons/Play.vue';
import Pause from 'vue-material-design-icons/Pause.vue';
import DotsHorizontal from 'vue-material-design-icons/DotsHorizontal.vue';
import Heart from 'vue-material-design-icons/Heart.vue';
import ClockTimeThreeOutline from 'vue-material-design-icons/ClockTimeThreeOutline.vue';

import { useSongStore } from '../stores/song'
import { storeToRefs } from 'pinia';
const useSong = useSongStore()
const { isPlaying, currentTrack, currentArtist, getCurrentArtistData, getCurrentTracks, loading } = storeToRefs(useSong)

// Computed để lấy artist data
const artist = computed(() => {
  return getCurrentArtistData.value || { name: 'Loading...', albumCover: '', tracks: [] }
})

// Computed để lấy tracks
const tracks = computed(() => {
  return getCurrentTracks.value || []
})

// Fetch dữ liệu từ API khi component mount
onMounted(async () => {
  if (useSong.artists.length === 0 && useSong.useApi) {
    await useSong.fetchArtistsFromAPI()
  }
})

const playFunc = () => {
    if (currentTrack.value) {
        useSong.playOrPauseThisSong(artist.value, currentTrack.value)
        return
    } 
    useSong.playFromFirst()
}
</script>

<template>
    <div class="p-8 overflow-x-hidden">
        <button
            type="button"
            class="text-white text-2xl font-semibold hover:underline cursor-pointer"
        >
            {{ artist.name }}
        </button>

        <div v-if="loading" class="text-white">Loading...</div>
        <div v-else-if="tracks.length === 0" class="text-white">No tracks available</div>
        
        <template v-else>
            <div class="py-1.5"></div>
            <div class="flex items-center w-full relative h-full">
                <img width="140" :src="artist.albumCover || '/images/albumCovers/default.png'">

                <div class="w-full ml-5">

                    <div
                        style="font-size: 33px;"
                        class="text-white absolute w-full hover:underline cursor-pointer top-0 font-bosemiboldld"
                    >
                        {{ artist.name }}
                    </div>

                    <div class="text-gray-300 text-[13px] flex">
                        <div class="flex">Album</div>
                        <div class="ml-2 flex" v-if="artist.releaseYear">
                            <div class="circle mt-2 mr-2" />
                            <span class="-ml-0.5">{{ artist.releaseYear }}</span>
                        </div>
                        <div class="ml-2 flex">
                            <div class="circle mt-2 mr-2" />
                            <span class="-ml-0.5">{{ tracks.length }} songs</span>
                        </div>
                    </div>

                    <div class="absolute flex gap-4 items-center justify-start bottom-0 mb-1.5">
                        <button class="p-1 rounded-full bg-white" @click="playFunc()">
                            <Play v-if="!isPlaying" fillColor="#181818" :size="25"/>
                            <Pause v-else fillColor="#181818" :size="25"/>
                        </button>
                        <button type="button">
                            <Heart fillColor="#1BD760" :size="30"/>
                        </button>
                        <button type="button">
                            <DotsHorizontal fillColor="#FFFFFF" :size="25"/>
                        </button>
                    </div>
                </div>
            </div>

            <div class="mt-6"></div>
            <div class="flex items-center justify-between px-5 pt-2">
                <div class="flex items-center justify-between text-gray-400">
                    <div class="mr-7">#</div>
                    <div class="text-sm">Title</div>
                </div>
                <div><ClockTimeThreeOutline fillColor="#FFFFFF" :size="18"/></div>
            </div>
            <div class="border-b border-b-[#2A2A2A] mt-2"></div>
            <div class="mb-4"></div>
            <ul class="w-full" v-for="(track, index) in tracks" :key="track.id">
                <SongRow :artist="artist" :track="track" :index="index + 1"/>
            </ul>
        </template>
    </div>
</template>

<style scoped>
    .circle {
        width: 4px;
        height: 4px;
        background-color: rgb(189, 189, 189);
        border-radius: 100%;
    }
</style>
