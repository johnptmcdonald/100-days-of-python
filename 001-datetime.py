from datetime import datetime
from datetime import date

todays_date = date.today()
todays_datetime = datetime.today()

todays_date.month

todays_datetime.month
todays_datetime.hour
todays_datetime.second

# date and datetime are two different objects that can't be subtracted from each other
# datetime is more useful as it has hours, minutes and seconds. 
