import json
from datetime import datetime
from datetime import timedelta

resorts = {
        "Breck": 0,
        "Vail": 0,
        "Keystone": 0,
        "Beaver Creek": 0
    }

with open('info.json','r') as f:
    
    seasons = json.loads(f.read())

    for season in seasons:
        days = season.get('PagedResult').get('List')
        for day in days:
            name = day.get('ResortName')
            resorts[name] += int(day.get('VerticalFeet'))


print(resorts)
