import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://www.billboard.com/charts/hot-100/"
Client_ID=os.getenv("CLIENT_ID")
Client_secret=os.getenv("CLIENT_SECRET")
REDIRECT_URI = "https://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=Client_ID,
        client_secret=Client_secret,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private"
    )
)

user = sp.current_user()
print(user["display_name"])

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

section_heading = soup.find("h1",id="section-heading").getText()
song_title_spans = soup.select("li ul li h3")

songs_names = [song.getText().strip() for song in song_title_spans]

