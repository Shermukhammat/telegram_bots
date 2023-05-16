import csv 
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

line_count = 0
titles = []
movies_dataset = []
with open('dataset_movies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if line_count != 0:
            titles.append(row[5])
            movies_dataset.append({'caption' : row[2], 'file_id' : row[1], 'title' : row[5]})
        line_count+=1


if __name__ == "__main__":
    acursy = fuzz.ratio("test", "fuiuiwbegftest")
    print(acursy)