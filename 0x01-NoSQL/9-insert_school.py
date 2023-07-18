#!/usr/bin/env python3
"""This module contains the function `insert_school`
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
