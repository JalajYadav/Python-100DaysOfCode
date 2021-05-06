Client_ID="<Your Spotify Client ID>"
Client_Secret="<Your Spotify Client_Secret>"

from bs4 import BeautifulSoup
from pprint import pprint
import requests
import spotipy

user_entered_date = input("Enter a date in YYYY-MM-DD format to obtain a playlist: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{user_entered_date}"

response = requests.get(url=billboard_url)
webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")

songs_list = [item.getText() for item in soup.find_all(name="span", class_="chart-element__information__song")]

print(songs_list)

# --------------------To get the auth token in a file[token.txt] run this code-----------------------------------------#
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID,
                                               client_secret=Client_Secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
# ---------------------------------------------------------------------------------------------------------------------#

user_id = sp.current_user()["id"]

song_uris=[]

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{user_entered_date.split('-')[0]}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_uris)

# ----------------------------------------------Create a playlist----------------------------------------------------#

playlist = sp.user_playlist_create(user_id,name=f"{user_entered_date} Billboard 100", public=False)
print("Playlist id: ",playlist['id'])

# ------------------------------------Add the song list to playlist---------------------------------------------------#
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)