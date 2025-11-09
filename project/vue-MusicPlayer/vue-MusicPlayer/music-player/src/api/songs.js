import { API_ENDPOINTS } from './config'

/**
 * Fetch danh sách bài hát từ Django API
 */
export async function fetchSongs() {
  try {
    const response = await fetch(API_ENDPOINTS.SONGS_LIST)
    if (!response.ok) {
      throw new Error('Failed to fetch songs')
    }
    return await response.json()
  } catch (error) {
    console.error('Error fetching songs:', error)
    throw error
  }
}

/**
 * Fetch danh sách bài hát được nhóm theo artist (tương tự artist.json)
 */
export async function fetchSongsGroupedByArtist() {
  try {
    const response = await fetch(API_ENDPOINTS.SONGS_GROUPED)
    if (!response.ok) {
      throw new Error('Failed to fetch grouped songs')
    }
    const data = await response.json()
    // Trả về artist đầu tiên nếu có, hoặc null
    return data.length > 0 ? data[0] : null
  } catch (error) {
    console.error('Error fetching grouped songs:', error)
    throw error
  }
}

/**
 * Fetch tất cả artists với tracks
 */
export async function fetchAllArtists() {
  try {
    const response = await fetch(API_ENDPOINTS.SONGS_GROUPED)
    if (!response.ok) {
      throw new Error('Failed to fetch artists')
    }
    return await response.json()
  } catch (error) {
    console.error('Error fetching artists:', error)
    throw error
  }
}

