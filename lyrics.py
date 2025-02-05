import requests


artist = "Dominic Fike"
song = "Frisk"
url = f"https://api.lyrics.ovh/v1/{artist}/{song}"

response = requests.get(url)
if response.status_code == 200:
    lyrics = response.json().get("lyrics", "Lyrics not found.")
    # print(f"Lyrics:\n{lyrics}")
else:
    print(f"Failed to fetch lyrics. Status code: {response.status_code}")

def extract_prechorus_and_chorus(lyrics):
    # Split lyrics into paragraphs (assuming each paragraph is separated by a newline)
    paragraphs = lyrics.strip().split("\n\n\n")

    # Extract 2nd and 3rd paragraphs if they exist
    if len(paragraphs) >= 3:
        prechorus = paragraphs[1]  # 2nd paragraph (index 1)
        chorus = paragraphs[2]      # 3rd paragraph (index 2)
        return prechorus, chorus
    else:
        return None, None

if(response.status_code == 200):
    prechorus , chorus = extract_prechorus_and_chorus(lyrics)

# print(prechorus)
    print(prechorus + '\n\n' + chorus)

else:
    print("sorry")