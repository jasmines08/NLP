# Lyrics Data Collection & Annotation

## Overview
This project collects Billboard Year-End Hot 100 songs, fetches their lyrics, and extracts key sections (prechorus & chorus) for further analysis. The dataset will be used for annotation.

---

## Data Collection Process
### 1. **Scraping Billboard Year-End Hot 100 Songs**
- We scrape Billboard's Year-End Hot 100 lists from Wikipedia for multiple years.
- The script (`songs.py`) extracts the **song title** and **artist name** from the Billboard chart table.
- Handles cases where multiple artists are listed (removes "featuring" and "and" to keep the primary artist).
- Saves the extracted data into text files (`top_100_songs_artists_YYYY.txt`), where `YYYY` is the year.

### 2. **Fetching Lyrics**
- The script (`dataCollect.py`) reads song titles and artists from `top_100_songs_artists_YYYY.txt`.
- It queries the **Lyrics.ovh API** (`https://api.lyrics.ovh/v1/`) to fetch lyrics.
- Extracts **prechorus & chorus** if available.
- Stores structured lyrics data in `song_lyrics.csv` with the following columns:
  - `song_id` – Unique identifier.
  - `artist` – Artist's name.
  - `title` – Song title.
  - `lyrics` – Extracted lyrics (prechorus + chorus, or full lyrics if extraction fails).
  - `emotion` – (Empty for now, to be labeled during annotation).
- A **2-second delay** is added between API calls to avoid rate limiting.

### 3. **Testing Lyrics Extraction**
- The script (`lyrics.py`) fetches lyrics for a **single test song** to validate extraction logic.

---

## Dataset Description
The dataset is stored in **CSV format** to ensure easy access. The dataset includes:
- **Unique instances:** 816
- **Total instances:** 960 (including 144 duplicate instances for annotator agreement calculation)
- **File format:** CSV (`data1.csv` to `data8.csv`)
- **Each instance represents:** One song’s prechorus & chorus (or full lyrics if extraction failed)

### Data Fields
| Column | Description |
|---------|-------------|
| `song_id` | Unique ID for each song |
| `artist` | Name of the artist |
| `title` | Title of the song |
| `lyrics` | Extracted lyrics (prechorus + chorus if available) |
| `emotion` | Empty column for manual annotation |

---

## Annotation Guidelines
- **Each annotator will label instances for 1 hour.**
- Estimate of time per instance: **30 seconds** (varies based on complexity).
- **Total annotation time:** `60 * 60 * 8 = 28,800 seconds`.
- **Estimated instances per 8-hour period:** `28,800 / 30 = 960 instances`.
- **Duplication for annotator agreement:** `960 * 0.15 = 144 instances` (duplicated for validation).
- **Final dataset distribution:**
  - **816 unique instances**.
  - **144 duplicate instances (for inter-annotator agreement calculations).**
  - **Split into 8 files (`data1.csv` to `data8.csv`).**
  - Duplicate instances are distributed across multiple files to ensure proper agreement analysis.
  - **8th file contains only unique instances** (ensuring no duplicate appears in it).

---

## Data Collection Considerations
- **Terms of Service Compliance:**
  - Lyrics are retrieved using the **Lyrics.ovh API**, which provides access under fair use conditions.
  - Wikipedia data is openly available for scraping but should be cited appropriately.
- **Dataset Licensing:**
  - If publishing, we must check if API content can be redistributed.
  - Billboard song lists are public information but should be credited properly.
- **Missing Data Handling:**
  - If lyrics are not found, the entry is **not stored** in the dataset.
  - Some extracted lyrics may not have prechorus/chorus sections, in which case **full lyrics** are used instead.

---

## Output Files
| File Name | Description |
|-----------|------------|
| `top_100_songs_artists_YYYY.txt` | List of top 100 songs & artists for a given year. |
| `song_lyrics.csv` | Raw dataset containing collected lyrics. |
| `data1.csv` – `data8.csv` | Final split dataset for annotation. |

---

## Future Improvements
- Implement **sentiment analysis** to classify the mood/emotion of lyrics.
- Expand data sources beyond Wikipedia and Lyrics.ovh API.
- Improve handling of missing or incomplete lyrics.
