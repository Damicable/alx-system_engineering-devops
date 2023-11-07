#!/usr/bin/python3
"""
This script defines a recursive function to query the Reddit API
"""

import requests
import sys

def recurse(subreddit, hot_list=[], after=None):
    """
    Return all hot article titles
    """

    headers = {'User-Agent': 'MyRedditBot/1.0'}  # Add your user-agent here

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None  # Invalid subreddit or other error

    data = response.json()
    if 'data' in data and 'children' in data['data']:
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])

    after = data['data']['after']

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


if __name__ == "__main__":
    recurse(sys.argv[1])
