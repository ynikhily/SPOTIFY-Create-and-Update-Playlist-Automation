from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# -----------------------------Using environment variables for Authorization ------------------------------
# You need to create spotipy client ID, spotipy client secret and redirect URI as environment variables
# that are used for authorization. Read Spotipy documentation for more info

# ---------------------------------------------VARIABLES-----------------------------------------------------

user_id = ""  # ENTER YOUR SPOTIFY USERNAME
playlist_name = ""  #ENTER THE PLAYLIST NAME WHICH EITHER EXISTS OR YOU WANT TO CREATE
scope = "playlist-read-private playlist-modify-private"
song_uri_list = []
date = input("Enter the date(in YYYY-MM-DD format) for which you want the top 100 billboard songs: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

# -------------------------------------------AUTHORIZATION---------------------------------------------------

auth_manager = SpotifyOAuth(scope=scope)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# -------------------------------------PLAYLIST CREATION/HANDLING------------------------------------------

playlist_response = spotify.current_user_playlists()
existing_playlists = {playlist['name']: playlist['id'] for playlist in playlist_response['items']}

if playlist_name not in existing_playlists:
    playlist = spotify.user_playlist_create(user=user_id, name=playlist_name, public=False)
    playlist_id = playlist['id']

else:
    playlist_id = existing_playlists[playlist_name]

# -----------------------------------SCRAPING THE BILLBOARD WEBSITE-----------------------------------------

response = requests.get(billboard_url)
soup = BeautifulSoup(response.text, "html.parser")
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

# -----------------------------FETCHING OF SONGS TO BE ADDED IN THE PLAYLIST-------------------------------

for song in all_songs:
    search_query = song.text.lower()
    year = date.split('-')[0]
    query = f'track: {search_query} year: {year}'
    song = spotify.search(query, 1, 0, "track")
    try:
        song_name = song['tracks']['items'][0]['name'].lower()
        if search_query in song_name:
            song_uri = song['tracks']['items'][0]['uri']
            song_uri_list.append(song_uri)

    except IndexError:
        print(f'Song: {search_query}\nStatus: Not Found')

# -----------------------------------------ADDING SONGS TO THE PLAYLIST--------------------------------------
spotify.playlist_add_items(playlist_id, song_uri_list)
