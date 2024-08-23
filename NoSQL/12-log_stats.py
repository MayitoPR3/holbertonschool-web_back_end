#!/usr/bin/env python3

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    # Connect to MongoDB
    try:
        client = MongoClient()
        db = client.logs
        collection = db.nginx
    except ConnectionFailure:
        print("Could not connect to MongoDB")
        return

    # Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count of each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of documents with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    main()
