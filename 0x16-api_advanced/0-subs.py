#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """
    Get number of subscribers for provided subreddit
    """
    if subreddit is None:
        return 0
    add = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "alx advanced api project"}

    resp = requests.get(add, headers=user_agent).json()
    ret_value = resp.get("data", {}).get("subscribers", 0)
    return ret_value
