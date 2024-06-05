#!/usr/bin/python3
"""number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'API Advanced (by /u/alx)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {}).get('subscribers', 0)
            return data
        else:
            return 0
    except requests.RequestException:
        return 0
    