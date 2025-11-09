// Django API configuration
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

export const API_ENDPOINTS = {
  SONGS_LIST: `${API_BASE_URL}/api/songs/list/`,
  SONGS_GROUPED: `${API_BASE_URL}/api/songs/grouped/`,
  SONGS: `${API_BASE_URL}/api/songs/`,
}

export default API_BASE_URL

