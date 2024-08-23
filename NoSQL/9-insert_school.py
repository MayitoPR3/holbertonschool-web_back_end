#!/usr/bin/env python3
""" 9. Insert a document in Python """

def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a
    collection based on kwargs
    """

    # Insert the document and get the result
    result = mongo_collection.insert_one(kwargs)

    # Return the _id of the new document
    return str(result.inserted_id)
