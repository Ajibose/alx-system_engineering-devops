#!/usr/bin/python3
"""
    Get subscribers to subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """Get total subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={'User-agent': 'Alx'})
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
