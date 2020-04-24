import json
from datetime import datetime
from datetime import timedelta


with open('lift.json','r') as f:
    
    days = json.loads(f.read())

    data = {}
    for day in days:
        lifts = day.get('LiftRides')
        date = day.get('Day').split('/')
        year = int(date[2])
        month =  int(date[1])

        if year == 2020:
            season = '19/20'
        elif year == 2019 and month == 12:
            season = '19/20'
        elif year == 2019:
            season = '18/19'
        elif year == 2018 and month == 12:
            season = '18/19'
        elif year == 2018:
            season = '17/18'
        elif year == 2017 and month == 12:
            season = '17/18'
        else:
            continue

        season_list = data.get(season, None)
        if not season_list:
            season_list = []
            data[season] = season_list

        for lift in lifts:
            season_list.append(lift.get('Lift'))

# Season 19/20

for season_name, value in data.items():
    d = {x:value.count(x) for x in value}
    for chair_name, amount in d.items():
        print(season_name, chair_name, amount, sep=",")

#print(data)
