from sklearn.metrics.pairwise import cosine_similarity

# Compute similarity matrix
similarity_matrix = cosine_similarity(df[features])

# Function to recommend songs based on similarity
def recommend_songs_content_based(input_song_name, df, similarity_matrix):
    if input_song_name not in df["track_name"].values:
        return "Song not found in dataset."

    song_idx = df[df["track_name"] == input_song_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[song_idx]))

    # Sort by highest similarity
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:11]

    recommended_indices = [i[0] for i in similarity_scores]
    return df.iloc[recommended_indices][["track_name", "track_artist"]]

# Example usage
recommendations = recommend_songs_content_based("Shape of You", df, similarity_matrix)
print(recommendations)
