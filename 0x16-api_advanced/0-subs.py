#!/usr/bin/python3
"""
    Get subscribers to subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """Get total subscribers"""
    base_url = "https://www.reddit.com"
    endpoint = f"/r/{subreddit}/about.json"
    response = requests.get(base_url + endpoint, headers={'user-agent': 'Alx'})
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0
