import http.client
import json
import time
import sys

from collections import namedtuple, Counter

# get a key from themoviedb.com
API_KEY = sys.argv[1]

Movie = namedtuple('Movie', 'id title original_language release_date')

def main():
	conn = http.client.HTTPSConnection("api.themoviedb.org")
	
	cnt = Counter()

	num_movies = 0

	for page in range(1, 19):
		conn.request('GET', '/3/discover/movie?api_key={}&sort_by=popularity.desc&primary_release_date.gte=2014&with_genres=18&page={}'.format(API_KEY, str(page)))

		res = conn.getresponse()
		data = res.read()
		data = json.loads(data)['results']

		for m in data:
			movie = Movie(id=int(m['id']), 
						  title=m['title'], 
						  original_language=m['original_language'], 
						  release_date=(m['release_date']))

			num_movies += 1
			print("\n")
			print(movie)
			cnt[movie.original_language] += 1

	print(cnt)
	print()
	print(cnt.most_common(5))
	
if __name__ == '__main__':
	main()


