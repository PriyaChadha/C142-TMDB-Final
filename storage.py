import csv

all_movies = []
#added encoding ='latin-1' because Python doesn't know how to decode some bytes from the original stream until you tell it what codec to use.
with open('final.csv', 'r',  encoding='latin-1') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []
