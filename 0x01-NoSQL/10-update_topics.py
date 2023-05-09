#!/usr/bin/env python3
""" a module for the update_topics function """


def update_topics(mongo_collection, name, topics):
    """
        Args:
            monmongo_collection: a pymongo collection object
            name: name of the school to be updated
            topics: list of topics to update

    """
    if len(topics) != 0:
        mongo_collection.update_one({'name': name}, {"$set": {'topics': topics}})
