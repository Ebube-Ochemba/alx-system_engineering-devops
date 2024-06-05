#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
    for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditClient/1.0 (by /u/bane116)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.ok:
        data = response.json().get('data').get('subscribers')
        return data if data else 0
    else:
        return 0
