#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""schools by topic"""


def schools_by_topic(mongo_collection, topic: str):
    """functiom that returns the list of school having a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
