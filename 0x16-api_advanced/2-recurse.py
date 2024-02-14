#!/usr/bin/python3
"""
This Python script uses recursive function
to querry the RedditAPI
"""

import requests as r


def recurse(subreddit, hot_list=[]):
    """
    This Function returns a list
    containing the titles of all hot articles
    for a given subreddit
    """
    
    after = None
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    response = r.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return hot_list
        else:
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            return recurse(subreddit, hot_list) + after
    else:
        return None
