import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "d23e845faea640d0bb83be5f1432db06"
CLIENT_SECRET = "e500964521be486abeecc52d9c4a6f60"
REDIRECT_URL = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id="d23e845faea640d0bb83be5f1432db06",
                                client_secret="e500964521be486abeecc52d9c4a6f60",
                                redirect_uri="http://example.com",
                                scope="playlist-modify-private"))


current_user = sp.current_user()['id']
