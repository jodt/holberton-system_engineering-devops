#!/usr/bin/python3
"""
This is the top_ten module
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    try:
        response = requests.get(
            url, headers=headers, params={
                'limit': '10'}, allow_redirects=False)
        jsonreponse = response.json()
        for post in (jsonreponse['data']['children']):
            print(post['data']['title'])
    except Exception:
        print(None)
