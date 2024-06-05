#!/usr/bin/python3
"""recurse"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles
    for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'API Advanced (by /u/alx)'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            after = data.get('after')
            children = data.get('children', [])
            hot_list.extend([post.get('data', {}).get('title')
                             for post in children])
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
