#!/usr/bin/python3
"""Top Ten"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'API Advanced (by /u/alx)'}
    params = {'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            for post in data:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except requests.RequestException:
        print(None)
