'''
PART 2: SIMILAR ACTROS BY GENRE
Using the imbd_movies dataset:
- Create a data frame, where each row corresponds to an actor, each column represents a genre, and each cell captures how many times that row's actor has appeared in that column’s genre 
- Using this data frame as your “feature matrix”, select an actor (called your “query”) for whom you want to find the top 10 most similar actors based on the genres in which they’ve starred 
- - As an example, select the row from your data frame associated with Chris Hemsworth, actor ID “nm1165110”, as your “query” actor
- Use sklearn.metrics.DistanceMetric to calculate the euclidean distances between your query actor and all other actors based on their genre appearances
- - https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html
- Output a CSV continaing the top ten actors most similar to your query actor using cosine distance 
- - Name it 'similar_actors_genre_{current_datetime}.csv' to `/data`
- - For example, the top 10 for Chris Hemsworth are:  
        nm1165110 Chris Hemsworth
        nm0000129 Tom Cruise
        nm0147147 Henry Cavill
        nm0829032 Ray Stevenson
        nm5899377 Tiger Shroff
        nm1679372 Sudeep
        nm0003244 Jordi Mollà
        nm0636280 Richard Norton
        nm0607884 Mark Mortimer
        nm2018237 Taylor Kitsch
- Describe in a print() statement how this list changes based on Euclidean distance
- Make sure your code is in line with the standards we're using in this class
'''

#Write your code below
import pandas as pd
import json
import sklearn.metrics import DistanceMetric
from datetime import datetime

def main():
    
    # Load the data
    with open('data/imdb_movies_2000to2022.prolific.json', 'r') as f:
        data = [json.loads(line) for line in f]

    # Create the genre-actor matrix
    actor_genre = {}
    for movie in data:
        for actor_id, actor_name in movie['actors']:
            if actor_name not in actor_genre:
                actor_genre[actor_name] = {genre: 0 for genre in movie['genres']}
            for genre in movie['genres']:
                actor_genre[actor_name][genre] += 1

    df = pd.DataFrame.from_dict(actor_genre, orient='index').fillna(0)

    # Select query actor
    query_actor = "Chris Hemsworth"

    # Calculate distances
    distances = DistanceMetric.get_metric('euclidean').pairwise(df.values)
    query_index = df.index.get_loc(query_actor)
    df['distance'] = distances[query_index]

    # Find the top 10 most similar actors
    top_10_similar = df.nsmallest(11, 'distance').drop(query_actor)
    top_10_similar = top_10_similar.iloc[:10]

    # Output the results to a CSV
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    top_10_similar.to_csv(f'data/similar_actors_genre_{current_datetime}.csv')

    # Print the result
    print("Top 10 most similar actors to Chris Hemsworth based on Euclidean distance:")
    print(top_10_similar.index)

if __name__ == "__main__":
    main()