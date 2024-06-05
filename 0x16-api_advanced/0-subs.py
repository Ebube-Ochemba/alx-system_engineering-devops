#!/usr/bin/python3
"""number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyRedditClient/1.0 (by /u/bane116)'}

    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json().get('data').get('subscribers')
        return data if data else 0
    else:
        return 0
