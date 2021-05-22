import requests
import json


def getApi():
    points = []
    for i in range(30):
        print(i+1)
        res = requests.get("https://qiita.com/api/v2/items",
                           params={"page": 1, "per_page": 100})
        points.append(json.loads(res.text))

    return points
