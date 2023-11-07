#!/usr/bin/python3
"""This defines a function that queries the Raddit API"""

import request
import sys


def number_of_subscribers(subreddit):
    """This query the API and returns the reddit subscribers"""
    if not subreddit:
        return 0

    # Reddit API URL for getting subreddit data

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # To avoid too many errors, set a custom User-Agent header
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        # A GET request to the Reddit API
        r = request.get(url, headers=headers, allow_redirects=False)

        # Check if response is successful and parse the json response
        if r.status_code == 200:
            data = r.json()

            subscribers = data['data']['subscribers']

            return subscribers
        else:
            return 0

    except r.RequestException:

        return 0


if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
