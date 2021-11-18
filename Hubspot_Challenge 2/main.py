import requests
import json
from collections import defaultdict
import datetime
from dateutil import parser
from Participants import Participants

"""
    Gets the partners list from the given api
"""
def get_partners():
    partners = requests.get("https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=4a13d97e711806f3414a32f57f81")
    return partners.json()


"""
    Given a date it returns the next day in ISO 8601 format.
"""
def get_next_day(date):
    curr_day = parser.parse(date)
    next_day = curr_day + datetime.timedelta(days=1)

    return next_day.strftime('%Y-%m-%d')


"""
    Gets the best date with the max number of participants for each country
"""
def get_attendees(partners):
    # To keep track of the dates where a partcipant can attend the 2-day event within each country
    attendence = defaultdict(lambda: defaultdict(list))
    countries = set()
    best_date_by_country = {}

    for partner in partners['partners']:
        dates = set(partner['availableDates'])
        country = partner['country']
        email = partner['email']
        countries.add(country)

        # For every date that the participant can attend ,we check if they can also attend the next day.
        for date in dates:
            if get_next_day(date) in dates:
                attendence[country][date].append(email)
                participants = Participants(
                    date, len(attendence[country][date]))

                # We also keep track of the best date that max number of participants can attend for each country
                if country not in best_date_by_country:
                    best_date_by_country[country] = participants
                else:
                    best_date_by_country[country] = max(best_date_by_country[country], participants)

    final_attendees = []

    for country in countries:
        if country in best_date_by_country:
            start_date = best_date_by_country[country].date
            final_attendees.append({
                "attendeeCount": best_date_by_country[country].total,
                "attendees": attendence[country][start_date],
                "name": country,
                "startDate": start_date
            })
        else:
            final_attendees.append({
                "attendeeCount": 0,
                "attendees": [],
                "name": country,
                "startDate": None
            })

    result = {}
    result['countries'] = final_attendees

    return result

"""
    Post the final attendee's list to the given api
"""
def send_invites(attendees):
    resp = requests.post("https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=4a13d97e711806f3414a32f57f81",data=json.dumps(attendees))
    print(resp)

def main():
    partners = get_partners()
    attendees = get_attendees(partners)
    send_invites(attendees)

if __name__ == "__main__":
    main()
