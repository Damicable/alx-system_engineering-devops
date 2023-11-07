#!/usr/bin/python3
"""This script defines a function that queries the Reddit API"""

import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API and prints the first 10 hot posts"""

    # Ensure that subreddit name is not empty
    if not subreddit:
        print("None")
        return

    # Reddit API URL for getting first 10 hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        # GET request to the Reddit API
        r = requests.get(url, headers=headers, allow_redirects=False)

        # Check if response is successfull and parse json response
        if r.status_code == 200:
            data = r.json()

            # Get posts list
            posts = data['data']['children']
            # Print the titles of the top 10
            for i, post in enumerate(posts[:10], 1):
                print(f"{i}. {post['data']['title']}")
        else:
            print("None")

    except requests.RequestException:
        # Handle any request exception
        print("None")


if __name__ == "__main__":
    top_ten(sys.argv[1])
