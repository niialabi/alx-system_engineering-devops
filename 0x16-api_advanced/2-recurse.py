#!/usr/bin/python3
"""
recursivley queries the Reddit API and
returns top10 hot of subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively get number of top10 hot of subscribers for provided subreddit
    """
    if subreddit is None:
        return None
    add = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "alx advanced api project"}

    resp = requests.get(add, params={"after": after}, headers=user_agent)

    if resp.status_code == 200:
        after = resp.json().get("data").get("after")
        if not after:
            return hot_list
        for post in resp.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
