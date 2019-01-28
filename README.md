#100-days-of-python

##Day 1
using the datetime module. 

```
from datetime import datetime
from datetime import date

datetime.today() # datetime.datetime(2019, 1, 28, 16, 44, 32, 147490)
date.today() 	 # datetime.date(2019, 1, 28)

// These are two different objects that can't be operated on together

// you can make your own date or datetime objects with `date(2019,12,12)` or `datetime(2019,12,12)`

// Subtraction of two date objects or two datetime objects will give you a `timedelta` object
```
