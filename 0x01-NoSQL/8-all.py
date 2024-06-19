#!/usr/bin/env/ python3

"""listing all documents in a collection"""

from typing import List


def list_all(mongo_collection) -> [List]:
    """function for listing all documnets in a collection"""
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents

