#!/usr/bin/python3
"""
    This Python script uses REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""


import requests as r
from sys import argv, exit

REST_API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        if argv[1].replace(".", "", 1).isdigit():
            id = int(argv[1])
            response = r.get(F'{REST_API_URL}/users/{id}').json()
            task_request = r.get(F'{REST_API_URL}/todos').json()
            emp_name = response.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_request))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            print(F'Employee {emp_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):')
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print(F'\t {task.get("title")}')
