# 100 days of python

## Day 1
Using the datetime module. 

```
from datetime import datetime
from datetime import date

datetime.today() # datetime.datetime(2019, 1, 28, 16, 44, 32, 147490)
date.today() 	 # datetime.date(2019, 1, 28)

// These are two different objects that can't be operated on together

// you can make your own date or datetime objects with `date(2019,12,12)` or `datetime(2019,12,12)`

// Subtraction of two date objects or two datetime objects will give you a `timedelta` object
```
## Day 2
Using datetime to log shutdown events

## Day 3
Using datetime and sleep to make a command line timer

## Day 4
Named tuples, default dict, counter, and deques. Deques are pretty good for random insertion/deletion because you can get away with moving fewer items from their previous position. Default dict is great for building up nested objects. Named tuples are like classless classes.  

## Day 5
Getting movie data, parsing it with csv.DictReader. Uses defaultdict, namedtuple ad Counter to manipulate data. 

## Day 6
Using namedtuple and counter to parse movie data from themoviedb.com

## Day 7
No py file, just list, tuple, dict basics

## Day 8
Parsing a nested DS in fun ways.
`sum(list_of_lists, [])` <-- this is a cool trick to flatten a list of lists







