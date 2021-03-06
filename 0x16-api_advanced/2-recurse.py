#!/usr/bin/python3
"""
This is the recurse module
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
    """
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    params = {}
    params['after'] = after
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        jsonreponse = response.json()
        after_key = jsonreponse['data']['after']
        if after_key is None:
            for post in (jsonreponse['data']['children']):
                hot_list.append(post['data']['title'])
            return hot_list
        hotlist = recurse(subreddit, hot_list, after_key)
        for post in (jsonreponse['data']['children']):
            hotlist.append(post['data']['title'])
        return hot_list
    except Exception:
        return None
