#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""inserting a document into a collection"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert(kwargs)
