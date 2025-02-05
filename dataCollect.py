import requests
import csv
import time
import re
import glob

def extract_prechorus_and_chorus(lyrics):
    # Split lyrics into paragraphs (assuming each paragraph is separated by a newline)
    paragraphs = lyrics.strip().split("\n\n\n")

    # Extract 2nd and 3rd paragraphs if they exist
    if len(paragraphs) >= 3:
        prechorus = paragraphs[1]  # 2nd paragraph (index 1)
        chorus = paragraphs[2]      # 3rd paragraph (index 2)
        return prechorus, chorus
    else:
        return "",""

# Function to fetch lyrics
def get_lyrics(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("lyrics", "")
    else:
        return ""

# List to store all songs from multiple years
songs = []

# Get all relevant text files (from 2016 to 2024)
files = glob.glob("top_100_songs_artists_*.txt")  # Matches files like top_100_songs_artists_2016.txt

# Process each file
for file_name in sorted(files):  # Sorting to maintain order from 2016 to 2024
    with open(file_name, 'r') as file:
        for line in file:
            match = re.match(r'Song: "(.*)", Artist: (.*)', line.strip())
            if match:
                title, artist = match.groups()
                songs.append({"artist": artist, "title": title})

# Collect lyrics and save to CSV
with open("song_lyrics.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["song_id", "artist", "title", "lyrics", "emotion"])  # Header

    for i, song in enumerate(songs):
        artist = song["artist"]
        title = song["title"]
        lyrics = get_lyrics(artist, title)
        if lyrics:
            prechorus , chorus = extract_prechorus_and_chorus(lyrics)
            if prechorus and chorus:
                part_lyrics = prechorus + '\n\n' + chorus
            else:
                part_lyrics = lyrics

            # Only save if lyrics are found
            print("lyric preview:", part_lyrics[:25])
            writer.writerow([i + 1, artist, title, part_lyrics, ""])  # Empty genre and emotion fields
            print(f"Saved lyrics for '{title}' by {artist}")

        time.sleep(2)  # Add delay to avoid rate limiting

print("Data collection complete.")