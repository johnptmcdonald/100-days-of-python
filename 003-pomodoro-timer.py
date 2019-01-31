from datetime import datetime
from time import sleep

def main():
	five = {'name': 'five', 'type': 'break', 'minutes': range(1, 6)}
	fifteen = {'name': 'fifteen', 'type': 'break', 'minutes': range(1, 16)}
	twenty_five = {'name': 'twenty five', 'type': 'work', 'minutes': range(1, 26)}

	schedules = [twenty_five, five, twenty_five, five, twenty_five, fifteen]

	for schedule in schedules:
		print('starting {} minutes of {} at {}'.format(schedule['name'], schedule['type'], datetime.today()))
		for minute in schedule['minutes']:
			print(minute, end =" ")
			for second in range(1,60):
				sleep(1)
				if second == 59:
					print('-')
				else:
					print('-', end="", flush=True)


if __name__ == '__main__':
	main()
