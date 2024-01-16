#!/usr/bin/python3
"""
Module: 100-count.py
this module contians a function that prints a sorted count of given
keywords
"""


import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    This function queries RedditApi
    Parses the title of the hot atricles
    Prints a sorted count of given keywords
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'RecursionParsing'}
    params = {'after': after} if after else {}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = respone.json()
    children = data['data']['children']
    titles = [post['data']['titles'].lower() for post in children]

    for title in titles:
        for word in word_list:
            if f" {word.lower()} " in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + 1

    after = data['data']['after']

    if after is not None:
        return count_words(subreddit, word_list, counts, after)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
