#!/usr/bin/python3
"""
a function that queries the Reddit API
prints the titles of the first 10 hot posts
listed for a given subreddit
"""
import requests


def top_ten(subred):
    """returns number of total subscribers"""
    url = ("https://api.reddit.com/r/{}?sort=hot&limit=10".format(subred))
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/senseiuc)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    response = response.json()
    if 'data' in response:
        for posts in response.get('data').get('children'):
            print(posts.get('data').get('title'))
    else:
        print(None)
