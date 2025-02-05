# Lyrics Data Collection

## Overview  
This project automates the collection of Billboard Year-End Hot 100 songs, fetches their lyrics, extracts key sections (prechorus & chorus), and structures the data into a CSV file for further analysis.  

## Project Structure  

### `songs.py` – Scrape Billboard Year-End Hot 100 Songs  
- Scrapes Billboard's **Year-End Hot 100** Wikipedia pages.  
- Extracts the **song title** and **artist name** from the table.  
- Handles cases where multiple artists are listed (e.g., removes "featuring" and "and" to keep the main artist).  
- Saves the song list to a `.txt` file (`top_100_songs_artists_YYYY.txt`), where `YYYY` represents the year.  

### `dataCollect.py` – Fetch Lyrics & Save Data  
- Reads song titles and artists from `top_100_songs_artists_YYYY.txt`.  
- Fetches lyrics using the **Lyrics.ovh API** (`https://api.lyrics.ovh/v1/`).  
- Extracts the **prechorus & chorus** from the lyrics (if available).  
- Saves the collected data into a **CSV file** (`song_lyrics.csv`) with the following columns:  
  - `song_id` – Unique identifier.  
  - `artist` – Name of the artist.  
  - `title` – Song title.  
  - `lyrics` – Extracted lyrics (either prechorus + chorus or full lyrics if extraction fails).  
  - `emotion` – (Currently empty, but can be used for sentiment analysis).  
- Includes a **2-second delay** between API calls to avoid rate limiting.  

### `lyrics.py` – Test Lyrics Fetching  
- Fetches lyrics for a single test song (`Dominic Fike - Frisky`).  
- Extracts **prechorus & chorus** and prints them.  
- Used for debugging and validating lyric extraction logic.  

## Output Files  
| File Name | Description |  
|-----------|------------|  
| `top_100_songs_artists_YYYY.txt` | List of top 100 songs & artists for a given year. |  
| `song_lyrics.csv` | Final dataset containing lyrics data. |  

## Future Improvements  
- Implement **sentiment analysis** to classify the mood/emotion of lyrics.  
- Expand data sources beyond Wikipedia and Lyrics.ovh API.  
- Improve handling of missing or incomplete lyrics.  

---
