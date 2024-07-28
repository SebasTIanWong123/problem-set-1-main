'''
Pull down the imbd_movies dataset here and save to /data as imdb_movies_2000to2022.prolific.json
You will run this project from main.py, so need to set things up accordingly
'''
import os
import requests
import json
import analysis_network_centrality
import analysis_similar_actors_genre

# Ingest and save the imbd_movies datase

def downloading_datasets(URL, save_path):

    response = requests.get(URL)
    if response.status_code == 200:
            with open(save_path, 'w') as file:
                 file.write(response.text)
            print(f'The Dataset has been downloaded and saved to {save_path}')
    else:
            print("Dataset failed to download")

def loading_dataset(file_path):
     data = []
     with open(file_path, 'r') as file:
          for line in file:
                try:
                    movie = json.laods(line)
                    data.aapned(movie)
                except json.JSONDecodeError as e:
                     print(f'JSON decoding has failed:{e}')
     return data

# Call functions / instanciate objects from the two analysis .py files
def main():

    URL = "https://github.com/cbuntain/umd.inst414/blob/main/data/imdb_movies_2000to2022.prolific.json?raw=true"
    save_path = os.path.join('data', 'imdb_movies_2000to2022.prolific.json')

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    downloading_datasets(URL, save_path)

    data = loading_dataset(save_path)


    analysis_network_centrality.run_analysis(data)
    analysis_similar_actors_genre.run_analysis(data)

if __name__ == "__main__":
    main()