from PyMemory import load_movi_data
from fuzzywuzzy import fuzz, process
import heapq


def search_movi(match, titles, movies_dataset):
    scores = {}
    lis = []

    n = 0
    for title in titles:
        score = fuzz.ratio(match, title.lower())
        scores[n] = score
        lis.append(score)
        n+=1

    respons = []
    Nlargest = heapq.nlargest(10, lis)
    for key, value in scores.items():
        if value in Nlargest:
            respons.append(movies_dataset[key])
    return respons

if __name__ == '__main__':
    titles, movies_dataset, line_count = load_movi_data()
    movies = search_movi("xalq", titles, movies_dataset)
    for movie in movies:
        print(movie['title'])

