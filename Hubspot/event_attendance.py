import json
from collections import defaultdict
import datetime
from dateutil import parser

with open("/Users/nipatel/Documents/Github/CTCI/CTCI/Hubspot/events.json") as f:
    partners = json.load(f)


# In a Separate File
class Participants:
    def __init__(self,date,total):
        self.date = date
        self.total = total

    def __gt__(self,other):
        if self.total == other.total:
            return self.date < other.date
        
        return self.total > other.total

# Inside Utils as a static method
def get_next_day(date):
    curr_day = parser.parse(date)
    next_day = curr_day + datetime.timedelta(days=1)

    return next_day.strftime('%Y-%m-%d')

best_date_by_country = {}
countries = set()
max_attendance = defaultdict(lambda :defaultdict(list))

for partner in partners['partners']:
    dates = set(partner['availableDates'])
    country = partner['country']
    email = partner['email']
    countries.add(country)
    for date in dates:
        if get_next_day(date) in dates:
            max_attendance[country][date].append(email)
            participants = Participants(date,len(max_attendance[country][date]))

            if country not in best_date_by_country:
                best_date_by_country[country] = participants
            else:
                best_date_by_country[country] = max(best_date_by_country[country],participants)

result = []

for country in countries:
    if country in best_date_by_country:
        start_date = best_date_by_country[country].date
        result.append({
            "attendeeCount":best_date_by_country[country].total,
            "attendees":max_attendance[country][start_date],
            "name":country,
            "startDate":start_date
        })
    else:
        result.append({
            "attendeeCount":0,
            "attendees":[],
            "name":country,
            "startDate":None
        })
# Have a main method
final_result = {}
# A Separate Class for response
final_result['countries'] = result
print(json.dumps(final_result))




    

