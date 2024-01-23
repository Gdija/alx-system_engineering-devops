#!/usr/bin/python3
"""recursion function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ list of hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "APIadv/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get("data").get("children")
    for post in posts:
        hot_list.append(post.get("data").get("title"))

    after = data.get("data").get("after")

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
