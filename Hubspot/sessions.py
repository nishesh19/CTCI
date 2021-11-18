import json
from collections import defaultdict
with open("/Users/nipatel/Documents/Github/CTCI/CTCI/Hubspot/sessions.json") as f:
    events = json.load(f)

visitors = defaultdict(list)
WINDOW_MILLISEC = 600000
for event in events["events"]:
    visitorId = event["visitorId"]
    url = event["url"]
    timestamp = event["timestamp"]

    visitors[visitorId].append((timestamp, url))

sessions = defaultdict(list)

for visitor, events in visitors.items():
    events = sorted(events)
    curr_pages = [events[0]]
    for timestamp, url in events[1:]:
        if timestamp - curr_pages[-1][0] <= WINDOW_MILLISEC:
            curr_pages.append((timestamp, url))
        else:
            sessions[visitor].append({
                "duration": curr_pages[-1][0]-curr_pages[0][0],
                "pages": list(map(lambda x:x[1],curr_pages)),
                "startTime": curr_pages[0][0]
            })
            curr_pages = [(timestamp, url)]

    sessions[visitor].append({
        "duration": curr_pages[-1][0]-curr_pages[0][0],
        "pages": list(map(lambda x:x[1],curr_pages)),
        "startTime": curr_pages[0][0]
    })

result = {}
result["sessionsByUser"] = {}

for user,session in sessions.items():
    result["sessionsByUser"][user] = session

print(json.dumps(result))
