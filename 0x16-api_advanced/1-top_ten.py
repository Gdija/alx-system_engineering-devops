#!/usr/bin/python3
""" retrieve titles data from a subreddit"""
import requests


def top_ten(subreddit):
    """print top 10 titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/kdj_g)"}
    params = {"limit": 10}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)
    if response.status_code == 200:
        data = response.json()
        if 'error' in data:
            print("None")
        else:
            top = data.get("data").get("children")
            for item in top:
                print(item.get("data").get("title"))
    else:
        print("None")
