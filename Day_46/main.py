from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint



date = "2000-12-31"
#input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = "2000"
#date.split('-')[0]
CLIENT_ID = "d23e845faea640d0bb83be5f1432db06"
CLIENT_SECRET = "e500964521be486abeecc52d9c4a6f60"
REDIRECT_URL = "http://example.com"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = "https://www.billboard.com/charts/hot-100/" + date

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                client_secret=CLIENT_SECRET,
                                redirect_uri=REDIRECT_URL,
                                show_dialog=True,
                                cache_path=".cache",
                                scope="playlist-modify-private"
                                ))


def get_billboard_song_names():
    response = requests.get(url=URL, headers=HEADER)
    html_page = response.text

    html_object = BeautifulSoup(html_page, 'html.parser')
    songs = html_object.select("li ul li h3")
    song_names = [song.getText(strip=True) for song in songs]
    return song_names    

def get_song_urls(song_names):
    song_uris = []
    for song in song_names:
        try:
            result = sp.search(q=f"track: {song} year: {year}", type="track")
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except Exception as exc:
            print(f"Erorr: {str(exc)}")
    print(song_uris)
    return song_uris        
     

def create_playlist(playlist_id, song_uris):
    user = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user, name=playlist_id, public=False)
    print(playlist)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)




songs_uri = get_song_urls(get_billboard_song_names())
#songs_uri = ['spotify:track:5j7E14lPXTzUpfTcZlDRtH', 'spotify:track:39iOGyDYl3At95ysYBbVpw', 'spotify:track:4ggdjiyOBVRDk0NzEwHQXn']
create_playlist(f"{date} Billboard 100", songs_uri)



   






