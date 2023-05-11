#!/usr/bin/env python3
""" a module for the get_item function """
import redis
import requests


def get_page(url: str) -> str:
    """ get_page track how many times a particular URL was accessed """

    cache = redis.Redis()
    search = redis.get(url)
    if search is None:
        