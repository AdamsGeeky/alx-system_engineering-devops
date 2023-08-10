#!/usr/bin/python3
"""
queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 102.0.5005.115'}
    link = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'limit': 10}
    res = requests.get(link, headers=user_agent, params=params)
    results = res.json()

    try:
        all_data = results.get('data').get('children')
        for data in all_data:
            print(data.get('data').get('title'))

    except Exception:
        print("None")
