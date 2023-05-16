from PyMemory import load_movi_data
from fuzzywuzzy import fuzz, process

titles, movies_dataset, line_count = load_movi_data()

n = 0
match = input("What are you searching?\n>>>")
presents = []
for title in titles:
    if n < 20:
        prosent = fuzz.ratio(match, title)
        print("------")
        print(f"index : {n}\nacursy : {prosent}%\ntitle : {title}")

    n+=1
    
