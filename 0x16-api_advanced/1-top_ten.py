#!/usr/bin/python3
""" queries the Reddit API and returns top10 hot of subreddit """

import requests


def top_ten(subreddit):
    """
    Get number of top10 hot of subscribers for provided subreddit
    """
    if subreddit is None:
        return 0
    add = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "alx advanced api project"}

    resp = requests.get(add, params={"limit": 10}, headers=user_agent)

    if resp.status_code == 200:
        for post in resp.json().get('data', {}).get('children', []):
            print(post.get('data').get('title'))
    else:
        print(None)
