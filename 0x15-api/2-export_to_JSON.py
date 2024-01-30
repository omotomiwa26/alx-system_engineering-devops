#!/usr/bin/python3
"""
    This Python export data
    in the JSON format.
"""


import csv
import json as j
import requests as r
from sys import exit, argv

REST_API_URL_USER_ID = 'https://jsonplaceholder.typicode.com/users/'


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py <USER_ID>")
        exit(1)
    USER_ID = argv[1]
    if not USER_ID.replace(".", "", 1).isdigit():
        print("Error: USER_ID must be a valid integer.")
        exit(1)
    USER_ID = int(argv[1])
    user_id_url = REST_API_URL_USER_ID + str(USER_ID)
    response = r.get(user_id_url)

    USERNAME = response.json().get('username')

    task_url = user_id_url + '/todos'
    response = r.get(task_url)
    tasks = response.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})

    """print (dict_data) as json file"""
    with open(F'{USER_ID}.json', 'w') as file:
        j.dump(dict_data, file)
