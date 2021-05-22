import requests
import json


def getApi():
    items = []
    params = {"page": 1, "per_page": 100}
    for i in range(60):
        print("fetching... page " + str(i+1))
        params["page"] = i + 1
        res = requests.get("https://qiita.com/api/v2/items", params=params)
        items.extend(json.loads(res.text))
        # print(res.text)

    return items
