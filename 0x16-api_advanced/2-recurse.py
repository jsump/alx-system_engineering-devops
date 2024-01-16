#!/usr/bin/python3
"""
Module: 2-recurse.py
This module contains a function that returns a list containing titles
of hot articles for a given subreddit
"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    This fucntion queries the Redit Api and returns a list containing
    all the titles of hot articles for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'USer-Agent': 'RecursiveBot v1.0'}
    params = {'after': after} if after else {}

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json()
    after = data['data']['after']
    children = data['data']['children']
    titles = [post['data']['title'] for post in children]
    hot_list.extend(titles)

    after = data['data']['after']

    if after is not none:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
