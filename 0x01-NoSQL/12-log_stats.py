#!/usr/bin/env python3
""" a script to find stats in logs.nginx collection """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx

    print(f'{col.count_documents({})} logs')
    print('Methods:')
    print(f'    method GET: {col.count_documents({"method": "GET"})}')
    print(f'    method POST: {col.count_documents({"method": "POST"})}')
    print(f'    method PUT: {col.count_documents({"method": "PUT"})}')
    print(f'    method PATCH: {col.count_documents({"method": "PATCH"})}')
    print(f'    method DELETE: {col.count_documents({"method": "DELETE"})}')
    print(f'{col.count_documents({"path": "/status"})} status check')