#!/usr/bin/env python3
"""
This module provides some displays log stats about Nginx logs stored in MongoDB

Database: logs
Collection: nginx
Display:
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
        5 lines with the number of documents with the method = [
            "GET", "POST", "PUT", "PATCH", "DELETE",
        ] in this order (it’s a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
"""
allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def display_logs(collection):
    """This function prints out the logs in the required format
    """
    print("{} logs".format(collection.count_documents({})))

    print("Methods:")
    for method in allowed_methods:
        count = len(list(collection.find({"method": method})))
        print("\tmethod {}: {}".format(method, count))

    get_with_status = len(list(collection.find(
        {"method": "GET", "path": "/status"}))
    )
    print("{} status check".format(get_with_status))


def main(collection):
    """Runs the main business logic"""
    display_logs(collection)


if __name__ == "__main__":
    from pymongo import MongoClient
    collection = MongoClient("mongodb://localhost:27017/").logs.nginx
    main(collection)
