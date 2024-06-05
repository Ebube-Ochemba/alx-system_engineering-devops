#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
    for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'bane116'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
    