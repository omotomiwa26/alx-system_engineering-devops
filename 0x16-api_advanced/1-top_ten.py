#!/usr/bin/python3
"""
This Python Script
queries the Reddit API
"""

import requests as r


def top_ten(subreddit):
    """
    This function returns and prints
    the titles of the first 10 hot posts
    listed for a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = r.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")
