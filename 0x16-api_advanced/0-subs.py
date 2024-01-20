#!/usr/bin/python3
"""
    Get subscribers to subreddit
"""


def number_of_subscribers(subreddit):
    """Get total subscribers"""
    import requests
    import sys
    base_url = "https://www.reddit.com"
    endpoint = f"/r/{sys.argv[1]}/about.json"
    response = requests.get(base_url + endpoint, headers={'user-agent': 'Alx'})
    if response.status_code == 404:
        return 0
    return response.json()["data"]["subscribers"]
