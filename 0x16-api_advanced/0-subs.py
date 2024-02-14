#!/usr/bin/python3
"""
This Python script
queries the Reddit API
"""


import requests as r


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers
    (not active users, total subscribers)
    for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = r.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
