#!/usr/bin/python3
"""
Module: 0-subs.py
This module contains a fucntion that returns the number of subscribers
for agiven subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """
    This function queries the RedditAPI: https://www.reddit.com/dev/api/
    It then returns the number of subscibers(active or not) for the subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'yourbotname'}  # custom agent set here
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # if the request failes
        return 0
