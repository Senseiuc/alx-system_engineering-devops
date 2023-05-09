#!/usr/bin/python3
"""
a function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subred):
    """returns number of total subscribers"""
    url = ("https://api.reddit.com/r/{}/about".format(subred))
    headers = {'User-Agent': 'RequestApi/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
