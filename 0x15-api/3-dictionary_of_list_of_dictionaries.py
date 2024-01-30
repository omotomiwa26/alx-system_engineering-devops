#!/usr/bin/python3
"""
    This Python script fetch Rest API
    for todo lists of employees
    and exports the data in the JSON format
"""


import json as j
import requests as r
from sys import argv, exit


REST_API_URL_USER = "https://jsonplaceholder.typicode.com/users"

if __name__ == '__main__':
    response = r.get(REST_API_URL_USER)
    Users = response.json()

    users_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        user_id_url = REST_API_URL_USER + F'/{USER_ID}'
        user_id_url = user_id_url + '/todos/'
        response = r.get(user_id_url)

        tasks = response.json()
        users_dict[USER_ID] = []
        for task in tasks:
            COMPLETED_TASKS_STATUS = task.get('completed')
            TITLE_TASKS = task.get('title')
            users_dict[USER_ID].append({
                "task": TITLE_TASKS,
                "completed": COMPLETED_TASKS_STATUS,
                "username": USERNAME
            })

            """Export To JSON """
    with open('todo_all_employees.json', 'w') as file:
        j.dump(users_dict, file)
