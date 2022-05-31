#!/usr/bin/python3
"""
This is the subs module
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        jsonresponse = response.json()
        return (jsonresponse['data']['subscribers'])
    except Exception:
        return 0
