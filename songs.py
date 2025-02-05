import requests
from bs4 import BeautifulSoup

# Send a GET request to the page
url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_2016'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table of interest (we're looking for the table with the class 'wikitable')
table = soup.find('table', {'class': 'wikitable'})

# Initialize an empty list to store the tuples (song, artist)
top_100 = []

# Iterate through the table rows (skip the header row)
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    
    if len(columns) >= 3:
        # Extract song name and artist name
        song_name = columns[1].get_text(strip=True)
        artist_name = columns[2].get_text(strip=True)

        if "featuring" in artist_name.lower():
            artist_name = artist_name.split("featuring")[0].strip()

        if "and" in artist_name.lower():
            artist_name = artist_name.split("and")[0].strip()

        # Append the song name and artist name as a tuple to the list
        top_100.append((song_name, artist_name))

# Save the list of top 100 songs and artists to a txt file
with open('top_100_songs_artists_2016.txt', 'w') as file:
    for song, artist in top_100:
        file.write(f"Song: {song}, Artist: {artist}\n")

print("Data has been saved to 'top_100_songs_artists.txt'")
