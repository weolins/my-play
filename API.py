import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= config.SPOTIPY_CLIENT_ID,
    client_secret= config.SPOTIPY_CLIENT_SECRET,
    redirect_uri= config.SPOTIPY_REDIRECT_URI,
    scope="user-library-read playlist-modify-private"))

results = sp.search(q="Two Feet", type="track", limit=5)
for track in results['tracks']['items']:
    print(track['name'], "-", track['artists'][0]['name'])