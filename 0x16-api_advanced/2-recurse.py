#!/usr/bin/python3
"""Module script to recursively returns list of hot posts of subreddit"""

import requests
import sys


def recurse(subreddit, hot_list=[], after=""):
    """
    Return all hot article titles list
    """
    req_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Switch value to prevent breaking"
    }
    params = {
        "after": after
    }
    r = requests.get(
            req_url, headers=headers, params=params, allow_redirects=False)
    if r.status_code == 200:
        bulk_resp = r.json()
        children = bulk_resp.get('data').get('children')
        new_after = bulk_resp.get('data').get('after')
        titles = list(map(lambda x: x.get('data').get('title'), children))
        hot_list.extend(titles)
        if new_after is None:
            return hot_list
        return recurse(subreddit, hot_list, new_after)
    else:
        return None


if __name__ == "__main__":
    recurse(sys.argv[1])
