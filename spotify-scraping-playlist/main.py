#Import
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Setup Spotify
SCOPE = "playlist-modify-private"
# --- CHANGE YOUR REDIRECT URI HERE AND MAKES SURE IT IS SAME AS IN YOUR SPOTIFY SETTING ---
REDIRECT_URL = "http://example.com"
# ---- CHANGE YOUR CLIENT ID AND SECRET FROM SPOTIFY HERE ---
CLIENT_ID = ""
CLIENT_SECRET = ""

# Initialize the Spotify client with user authentication. The specified scope allows for modifying private playlists.
sp = spotipy.Spotify(
	auth_manager=SpotifyOAuth(
		scope=SCOPE,
		client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET,
		redirect_uri=REDIRECT_URL))

# Extract user id of spotify
USER_ID = sp.current_user()["id"]

# Setup Billboard
date_time = input("Enter the time you want to travel back? Type in YYYY-MM-DD format:  ")
year = date_time.split("-")[0]
# The BillBoard link changes based on user's date
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date_time}/"

# Scrapping BillBoard
billboard_response = requests.get(BILLBOARD_URL)
billboard_web_text = billboard_response.text

soup = BeautifulSoup(billboard_web_text, "html.parser")

heading_all = soup.select("div ul li ul li h3")

# The list contain title of each songs
song_list = [title.getText().strip() for title in heading_all]
print("Scrapping done.")

# To deal with Spotify, generate list of songs's uri (resource identifier)
print("Compiling URI list...")
song_uri = []
for song in song_list:
	result = sp.search(q=f"track:{song} year:{year}", type="track")
	try:
		uri = result["tracks"]["items"][0]["uri"]
		song_uri.append(uri)
	except Exception as E:
		print(f"{song} does not exists in Spotify. Skipped...")
print("URI list completed.")

# Create spotify playlist
playlist = sp.user_playlist_create(user=USER_ID, name=f"{date_time} Billboard 100" , public=False, collaborative=False, description="100 top songs from Billboard")
print("Playlist created.")

# Add songs to created playlist
sp.user_playlist_add_tracks(user=USER_ID, playlist_id=playlist["id"], tracks=song_uri, position=None)
print("Playlist updated!")
