#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""updating a document in a collection"""


def update_topics(mongo_collection, name, topics):
    """function that update a doucument in a collection base on name"""
    return mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}})
