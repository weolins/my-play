import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("high_popularity_spotify_data.csv")

# Display basic information
print(df.info())
print(df.head())

columns_to_keep = [
    "energy", "tempo", "danceability", "loudness", "liveness", "valence",
    "instrumentalness", "speechiness", "acousticness", "track_popularity",
    "track_name", "track_artist", "track_album_name", "track_album_release_date",
    "playlist_genre", "playlist_subgenre", "mode", "key"
]

df = df[columns_to_keep]

df.to_csv("final.csv", mode="a", header=False, index=False)
