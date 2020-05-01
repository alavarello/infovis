import json
from datetime import datetime
from datetime import timedelta

all_seasons_days_in_week = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0

 } 

with open('info.json','r') as f:
    
    seasons = json.loads(f.read())
    days = seasons[2].get('PagedResult').get('List')

    for day in days:
        date = day.get('Date')
        date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
        all_seasons_days_in_week[date.weekday()] += int(day.get('VerticalFeet'))
        print(date)

total = sum(all_seasons_days_in_week.values())
for day, vertical_meters in all_seasons_days_in_week.items():
    all_seasons_days_in_week[day] = round((vertical_meters/total) * 100)


print(all_seasons_days_in_week)