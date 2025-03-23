import requests  # Import requests to fetch webpage data
from bs4 import BeautifulSoup  # Import BeautifulSoup for web scraping
import spotipy  # Import Spotipy to interact with the Spotify API
from spotipy.oauth2 import SpotifyOAuth  # Import SpotifyOAuth for authentication

# Spotify API credentials (Replace with your actual credentials)
client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'

# Prompt the user to enter a date in YYYY-MM-DD format
date = input('Which date do you want to travel to? Type the date in YYYY-MM-DD format.\n')

# Construct the Billboard URL for the given date
URL = f'https://www.billboard.com/charts/hot-100/{date}/'

# Send a request to the Billboard website
response = requests.get(url=URL)

# Parse the webpage content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Select all song titles using the appropriate HTML tag
songs_list = soup.select('li h3')

# Initialize an empty list to store song names
songs = []
for song in songs_list:
    songs.append(song.string)  # Extract song text

# Remove None values (caused by empty elements in the list)
none_count = songs.count(None)
for _ in range(none_count):
    songs.pop()

# Clean up song names by removing extra spaces and special characters
for i in range(len(songs)):
    songs[i] = songs[i].replace('\t', '').replace('\n', '').strip()

# Print the extracted song names for verification
print(songs)

# Authenticate and connect to Spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # Scope for modifying private playlists
        redirect_uri="http://example.com",  # Redirect URI (must match the one in your Spotify app settings)
        client_id=client_id,  # Your Spotify Client ID
        client_secret=client_secret,  # Your Spotify Client Secret
        show_dialog=True,  # Show authentication dialog
        cache_path="token.txt",  # Path to store authentication token
        username='YOUR SPOTIFY USERNAME',  # Your Spotify username
    )
)

# Get the current authenticated user ID
user_id = sp.current_user()["id"]

# Initialize a list to store Spotify track URIs
song_uris = []
# Extract the year from the input date
year = date.split("-")[0]

# Search for each song on Spotify and collect its URI
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")  # Search for the song in the given year
    print(result)  # Print search results for debugging
    try:
        uri = result["tracks"]["items"][0]["uri"]  # Extract the first track URI
        song_uris.append(uri)  # Add it to the list
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")  # Handle songs not found on Spotify

# Create a new private playlist with the given date in the name
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)  # Print playlist details for verification

# Add the collected songs to the newly created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
