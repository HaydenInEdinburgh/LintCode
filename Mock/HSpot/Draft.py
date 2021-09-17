import requests

if __name__ == '__main__':
    data_url = 'https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=be846993709aa5dd087f1847e272'
    r = requests.get(data_url).json()
    print(r['events'])