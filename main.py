import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'

date = input('Which date do you want to travel to? Type the date in YYYY-MM-DD format.\n')

URL = f'https://www.billboard.com/charts/hot-100/{date}/'

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, 'html.parser')
songs_list = soup.select('li h3')
songs = []
for song in songs_list:
    songs.append(song.string)

none_count = songs.count(None)

for _ in range(none_count):
    songs.pop()

for i in range(len(songs)):
    songs[i] = songs[i].replace('\t', '').replace('\n', '').strip()
print(songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username='YOUR SPOTIFY USERNAME',
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
