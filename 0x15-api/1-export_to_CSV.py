#!/usr/bin/python3
"""
    This Python script export data
    in CSV format
"""
import csv as c
import requests as r
from sys import argv, exit

REST_API_URL_USER = 'https://jsonplaceholder.typicode.com/users/'

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <user_id>")
        exit(1)
    user_id = argv[1]
    if not user_id.replace(".", "", 1).isdigit():
        print("Error: User ID must be a valid integer.")
        exit(1)
    user_id = int(argv[1])
    user_url = REST_API_URL_USER + str(user_id)
    response = r.get(user_url)
    user_name = response.json().get('username')
    task = user_url + '/todos'
    response = r.get(task)
    tasks = response.json()

    with open(F'{user_id}.csv', 'w') as file:
        for task in tasks:
            completed = task.get('completed')
            task_title = task.get('title')

            """print as Csvfile"""
            file.write(F'"{user_id}","{user_name}",'
                          F'"{completed}","{task_title}"\n')
