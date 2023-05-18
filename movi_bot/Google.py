from PyMemory import load_movi_data
from fuzzywuzzy import fuzz, process
import heapq
import time


def search_movi(match, titles = None, limt = 10):
    titles
    scores, indexs = [], []

    for title in titles:
        scores.append(fuzz.ratio(match.lower(), title.lower()))
        
    for n in range(limt):
        maxs = max(scores)
        indexs.append(scores.index(maxs))
        scores.remove(maxs)
    return indexs

    

if __name__ == '__main__':
    # start_time = time.time()
    titles, movies_dataset, line_count = load_movi_data()
    start_time = time.time()

    indexs = search_movi("zorro", titles = titles)
    for index in indexs:
        print(movies_dataset[index]['title'])

    print(f"{time.time() - start_time}")

