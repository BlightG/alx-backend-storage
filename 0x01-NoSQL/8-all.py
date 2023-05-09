#!/usr/bin/env python3
""" a module for the list_all function """


def list_all(mongo_collection) -> list:
    """
        Args:
            mongo_collection: a pymongo collection object

        Return: a list of documents in @mongo_collection object
                or an empty list
    """

    cursor = mongo_collection.find({})
    results = list(cursor)
    if len(results) == 0:
        return results
    else:
        return [result for result in results]
