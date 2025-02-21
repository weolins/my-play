import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("low_popularity_spotify_data.csv")

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

numerical_features = [
    "energy", "tempo", "danceability", "loudness", "liveness", "valence",
    "instrumentalness", "speechiness", "acousticness", "track_popularity"
]

scaler = MinMaxScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])

df = pd.get_dummies(df, columns=["playlist_genre", "playlist_subgenre"])
encoder = LabelEncoder()
df["track_artist"] = encoder.fit_transform(df["track_artist"])
df["track_album_name"] = encoder.fit_transform(df["track_album_name"])

df["track_album_release_date"] = pd.to_datetime(df["track_album_release_date"], errors="coerce")
df["release_year"] = df["track_album_release_date"].dt.year
df.drop(columns=["track_album_release_date"], inplace=True)

df.to_csv("final.csv", mode="a", header=False, index=False)
