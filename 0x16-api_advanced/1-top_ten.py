#!/usr/bin/python3
"""
Module: 1-top_ten.py
This module contains a function that prints the titles of hot posts
"""


import requests


def top_ten(subreddit):
    """
    This function queries the Reddit Api and prints the titles
    of the first 10 hot posts listed for s given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'HotPostsBot v1.0'}  # Setting custom user-agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        titles = [post['data']['title'] for post in data['data']['children']]
        for title in titles:
            print(title)
    else:
        return None
