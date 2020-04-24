import json
from datetime import datetime
from datetime import timedelta

vertical_feets = []

with open('info.json','r') as f:
    
    seasons = json.loads(f.read())

    sum = 0
    days = seasons[2].get('PagedResult').get('List')
    days.reverse()
    last_date = days[0].get('Date')
    last_date = datetime.strptime('12/14/2017 12:00:00', '%m/%d/%Y %H:%M:%S')
    print('Season19/20')

    for day in days:
    	date = day.get('Date')
    	date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')

    	last_date += timedelta(days=1)
    	while last_date < date:
    		vertical_feets.append(sum)
    		last_date += timedelta(days=1)


    	sum += int(day.get('VerticalFeet'))
    	vertical_feets.append(sum)


print(vertical_feets)
