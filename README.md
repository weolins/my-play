# Spotify Playlist Generator AI

## Description
Spotify Playlist Generator AI is a Python-based project that generates personalized Spotify playlists based on 1-5 seed songs. It leverages machine learning to analyze song attributes such as tempo, energy, and mood, and integrates with the Spotify API to create and save playlists directly to a user's account.

---

## Features
- Generate playlists using 1-5 seed songs.
- Analyze and compare audio features like danceability, energy, valence, and tempo.
- Integrate with Spotify to fetch recommendations and save playlists directly to the user’s account.

---

## Getting Started

### Prerequisites
- Python 3.9 or above
- Spotify Developer Account (to access the Spotify API)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/weolins/my-play.git
   cd my-play
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Spotify API credentials:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create an app.
   - Copy the `Client ID` and `Client Secret`.
   - Create a `.env` file in the project root and add:
     ```
     SPOTIPY_CLIENT_ID=your_client_id
     SPOTIPY_CLIENT_SECRET=your_client_secret
     SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
     ```

4. Run the app:
   ```bash
   python app.py
   ```

---

## Usage
1. Launch the app by running the above command.
2. Enter 1-5 seed songs in the input field.
3. Click "Generate Playlist" to create a playlist based on your input.
4. Optionally, save the playlist directly to your Spotify account.

---

## Credits
- This project uses the [Spotify Music Dataset](https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset), licensed under the [Database Contents License (DbCL) v1.0](https://opendatacommons.org/licenses/dbcl/1-0/).

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the Apache 2.0 License. See the [LICENSE](https://github.com/weolins/my-play/blob/main/LICENSE) file for details.

---

## Acknowledgments
- [Spotify Music Dataset](https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset)
- [Spotipy Library](https://spotipy.readthedocs.io/)
- [Flask](https://flask.palletsprojects.com/)
- [Streamlit](https://streamlit.io/) (if used for the UI)

