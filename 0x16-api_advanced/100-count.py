#!/usr/bin/python3
"""
This Python Script
that queries the Reddit API
"""

from collections import defaultdict as d
import requests as r


def count_words(subreddit, word_list):
    """
    This uses recursive function and parses
    the title of all hot articles, and prints
    a sorted count of given keywords
    """

    after = None
    counts = None

    if counts is None:
        counts = d(int)

    url = F"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    response = r.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(F"{word.lower()}: {count}")
            return
        else:
            for post in posts:
                title = post['data']['title']
                words = title.lower().split()
                for word in word_list:
                    if word.lower() in words:
                        counts[word.lower()] += words.count(word.lower())
            after = data['data']['after']
            count_words(subreddit, word_list) + after + counts
    else:
        return ""
