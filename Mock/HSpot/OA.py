from collections import defaultdict
import json
import requests

win_sec = 600000

def generate_function(dataset):
    raw_data = defaultdict(list)
    for eve in dataset['events']:
        record = (eve['timestamp'], eve['url'])
        raw_data[eve['visitorId']].append(record)

    output = {}
    for user, events in raw_data.items():
        sessions = []
        events = sorted(events)
        startTime, url = events[0]
        endTime, pages = startTime, [url]

        for i in range(1, len(events)):
            timestamp, url = events[i]
            if timestamp <= endTime + win_sec:
                pages.append(url)
                endTime = timestamp
            else:
                add(startTime, endTime, pages, sessions)
                pages = [url]
                startTime = endTime = timestamp

        if pages:
            add(startTime, endTime, pages, sessions)

        output[user] = sessions
    return {'sessionsByUser': output}


def add(startTime, endTime, pages, sessions):
    sessions.append(
        {
            'duration': endTime - startTime,
            'pages': pages,
            'startTime': startTime
        }
    )

if __name__ == '__main__':
    data_url = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=be846993709aa5dd087f1847e272'
    input = requests.get(data_url).json()
    results = json.dumps(generate_function(input), indent=2)
    return_url = 'https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=be846993709aa5dd087f1847e272'
    r = requests.post(return_url, data=results)
    print(r.text)