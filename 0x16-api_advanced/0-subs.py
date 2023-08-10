#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user_agent = {'User-agent': 'Google Chrome Version 102.0.5005.115'}
    link = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(link, headers=user_agent)
    results = res.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
