from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
	""" 
	Extracts movies from csv and stores them in a dict
	where keys are directors and values is a list of Movie namedtuples		
	"""
	directors = defaultdict(list)

	with open(data, encoding='utf-8') as f:
		# DictReader just puts the row data into an ordered dict
		for line in csv.DictReader(f):
			try:
				director = line['director_name']
				movie = line['movie_title'].replace('\xa0', '')
				year = int(line['title_year'])
				score = float(line['imdb_score'])
			except ValueError:
				continue

			m = Movie(title=movie, year=year, score=score)
			directors[director].append(m)

	return directors

directors = get_movies_by_director()

# counter is just a dict for counting
cnt = Counter()

for director, movies in directors.items():
	cnt[director] += len(movies)

print(cnt.most_common(10))

