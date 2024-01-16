#!/usr/bin/python3
""" retrieve subscribers data from a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'User-Agent': 'linux:0x16.api.advanced:v1.0.0(by /u/kdj_g)'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        subs = response.json()
        return subs.get('data').get('subscribers')
    else:
        return 0


if __name__ == '__main__':
    number_of_subscribers(subreddit)
