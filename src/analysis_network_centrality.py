'''
PART 1: NETWORK CENTRALITY METRICS

Using the imbd_movies dataset
- Guild a graph and perform some rudimentary graph analysis, extracting centrality metrics from it. 
- Below is some basic code scaffolding that you will need to add to. 
- Tailor this code scaffolding and its stucture to however works to answer the problem
- Make sure the code is line with the standards we're using in this class 
'''
import json
import numpy as np
import pandas as pd
import networkx as nx
from datetime import datetime

def main():
# Build the graph
    g = nx.Graph()

# Set up your dataframe(s) -> the df that's output to a CSV should include at least the columns 'left_actor_name', '<->', 'right_actor_name'
    df = pd.DataFrame(columns=['left_actors_name', '<->', 'right_actor_name'])

with open('data/imdb_movies_2000to2022.prolific.json', 'r') as in_file:
    # Don't forget to comment your code
    for line in in_file:
        # Don't forget to include docstrings for all function
        # Load the movie from this line
        this_movie = json.loads(line)
            
        # Create a node for every actor
        for actor_id,actor_name in this_movie['actors']:
            g.add_node(actor_name)
        # add the actor to the graph    
        # Iterate through the list of actors, generating all pairs
        ## Starting with the first actor in the list, generate pairs with all subsequent actors
        ## then continue to second actor in the list and repeat
        actors = this_movie['actors']
        for i, (left_actor_id, left_actor_name) in enumerate(actors):
            for right_actor_id, right_actor_name in actors[i +1]:
                if g.has_edge(left_actor_name, right_actor_name):
                    g[left_actor_name][right_actor_name]['weight'] += 1
                else:
                    g.add_edge(left_actor_name, right_actor_name, weight=1)

                df = df.append({'left_actor_name': left_actor_name, '<->': '<->', 'right_actor_name': right_actor_name}, ignore_index=True)


    print("Nodes:", len(g.nodes))
    print("Edges:", len(g.edges))

    centrality = nx.degree_centrality(g)
    top_ten_central = sorted(centrality.items(), key=lambda item: item[1], reverse=True)[:10]
    print("The Top Ten Most Central Nodes:", top_ten_central)

    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_csv(f'data/network_centrality_{current_datetime}.csv', index=False)

if __name__  == "__main__":
    main()

