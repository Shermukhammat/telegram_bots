import csv 

def load_movi_data():
    line_count = 0
    titles = []
    movies_dataset = []
    with open('dataset/movies.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count != 0:
                titles.append(row[5])
                movies_dataset.append({'caption' : row[2], 'file_id' : row[1], 'title' : row[5], 'id' : row[4], 'message_id' : row[0], 'photo' : row[6]})
            line_count+=1
    print("Movies databes sucsesfuly conected ...")
    return titles, movies_dataset, line_count


if __name__ == "__main__":
    titles, movies_dataset, line_count = load_movi_data()
    for title in movies_dataset[:10]:
        print(title['photo'])
    