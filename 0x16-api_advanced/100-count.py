#!/usr/bin/python3
"""count"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Counts occurrences of given keywords in hot articles' titles"""

    # Initialize word_count dictionary on first call
    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'API Advanced (by /u/alx)'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    try:
        data = response.json().get('data', {})
        after = data.get('after')
        children = data.get('children', [])

        for post in children:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_count:
                word_count[word] += title.split().count(word)
    except requests.RequestException:
        return None

    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        # Sort the results
        words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in words:
            if count > 0:
                print("{}: {}".format(word, count))

    return None
