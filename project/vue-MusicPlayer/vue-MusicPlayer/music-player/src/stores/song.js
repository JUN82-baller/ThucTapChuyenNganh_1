import { defineStore } from 'pinia'
import artist from '../artist.json'
// import { fetchSongsGroupedByArtist } from '../api/songs'

export const useSongStore = defineStore('song', {
  state: () => ({
    isPlaying: false,
    audio: null,
    currentArtist: null,
    currentTrack: null,
    artists: [], // Danh sách artists từ API
    useApi: true, // Flag để chuyển đổi giữa API và local data
    loading: false,
    error: null
  }),
  
  getters: {
    // Lấy artist hiện tại hoặc artist đầu tiên
    getCurrentArtistData() {
      if (this.useApi && this.artists.length > 0) {
        return this.currentArtist || this.artists[0]
      }
      return this.currentArtist || artist
    },
    
    // Lấy tracks của artist hiện tại
    getCurrentTracks() {
      const artistData = this.getCurrentArtistData
      return artistData?.tracks || []
    }
  },
  
  actions: {
    // Fetch artists từ API
    async fetchArtistsFromAPI() {
      this.loading = true
      this.error = null
      try {
        const response = await fetch('http://127.0.0.1:8000/api/songs/grouped/')
        if (!response.ok) {
          throw new Error('Failed to fetch artists from API')
        }
        const data = await response.json()
        this.artists = data
        this.useApi = true
        // Nếu chưa có currentArtist, set artist đầu tiên
        if (!this.currentArtist && data.length > 0) {
          this.currentArtist = data[0]
        }
      } catch (error) {
        console.error('Error fetching artists from API:', error)
        this.error = error.message
        // Fallback về local data
        this.useApi = false
        this.currentArtist = artist
      } finally {
        this.loading = false
      }
    },
    
    // Sử dụng local data (artist.json)
    useLocalData() {
      this.useApi = false
      this.currentArtist = artist
    },
    
    loadSong(artist, track) {
        this.currentArtist = artist
        this.currentTrack = track

        /*run if this.audio exist and not null*/
        if (this.audio && this.audio.src) {
            this.audio.pause()
            this.isPlaying = false
            this.audio.src = ''
        }

        this.audio = new Audio()
        // Sử dụng path từ API hoặc local
        this.audio.src = track.path

        setTimeout(() => {
            this.isPlaying = true
            this.audio.play()
        }, 200)
    },

    playOrPauseSong() {
        if (!this.audio) return
        if (this.audio.paused) {
            this.isPlaying = true
            this.audio.play()
        } else {
            this.isPlaying = false
            this.audio.pause()
        }
    },

    playOrPauseThisSong(artist, track) {
        /*If no song is played, load new song, else play or pause song */
        if (!this.audio || !this.audio.src || (this.currentTrack?.id !== track.id)) {
            this.loadSong(artist, track)
            return
        }

        this.playOrPauseSong()
    },

    prevSong(currentTrack) {
        const tracks = this.getCurrentTracks
        if (!tracks || tracks.length === 0) return
        
        if (currentTrack.id === tracks[0].id) {
            // Nếu đang ở track đầu tiên, quay về track cuối
            let track = tracks[tracks.length - 1]
            this.loadSong(this.getCurrentArtistData, track)
        } else {
            // Tìm track trước đó
            const currentIndex = tracks.findIndex(t => t.id === currentTrack.id)
            if (currentIndex > 0) {
                let track = tracks[currentIndex - 1]
                this.loadSong(this.getCurrentArtistData, track)
            }
        }
    },

    nextSong(currentTrack) {
        const tracks = this.getCurrentTracks
        if (!tracks || tracks.length === 0) return
        
        const currentIndex = tracks.findIndex(t => t.id === currentTrack.id)
        if (currentIndex === tracks.length - 1) {
            // Nếu đang ở track cuối, quay về track đầu
            let track = tracks[0]
            this.loadSong(this.getCurrentArtistData, track)
        } else {
            // Track tiếp theo
            let track = tracks[currentIndex + 1]
            this.loadSong(this.getCurrentArtistData, track)
        }
    },

    playFromFirst() {
        this.resetState()
        const tracks = this.getCurrentTracks
        if (tracks && tracks.length > 0) {
            let track = tracks[0]
            this.loadSong(this.getCurrentArtistData, track)
        }
    },

    resetState() {
        this.isPlaying = false
        this.audio = null
        this.currentArtist = null
        this.currentTrack = null
    }
  },
  persist: true
})
