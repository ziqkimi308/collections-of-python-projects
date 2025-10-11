# Spotify Playlist from Billboard's 100 Top Songs

- This project automates the creation of a Spotify playlist based on the Billboard Hot 100 chart for a user-specified date. By scraping the Billboard website and using the Spotify API, it compiles the chart-topping songs into a private playlist on the user's Spotify account.

---

### Features:

- Billboard Hot 100 Scraping: Retrieves the top 100 songs from the Billboard website for any given date.
- Spotify Integration: Automatically searches for tracks on Spotify and compiles them into a playlist.
- Date-Specific Playlists: Travel back in time by specifying a date and get the hits from that era.
- Error Handling: Skips tracks that cannot be found on Spotify and continues building the playlist.

---

### How It Works:

- Prompts the user to input a date in YYYY-MM-DD format.
- Scrapes the Billboard Hot 100 songs for that date.
- Searches for the songs on Spotify.
- Creates a new private playlist and adds the found songs.

---

# Dependencies:

- Requests: To fetch data from Billboard and Spotify.
- BeautifulSoup4: For web scraping Billboard charts.
- Spotipy: Spotify API integration.

---

### Screenshots:

<img width="1273" alt="image" src="https://github.com/user-attachments/assets/e9292a9a-47ee-4bb2-8ad8-1c12441215e8" />
<br>
<img width="1273" alt="image" src="https://github.com/user-attachments/assets/2fa38c73-f34c-4324-903a-72f5f8b37ead" />

