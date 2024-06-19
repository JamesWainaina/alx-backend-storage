#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods: ")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
        count_status_check = logs_collection.count_documents(
            {"method": "GET",
             "path": "/status"
             })
        print(f"{count_status_check} status check")
