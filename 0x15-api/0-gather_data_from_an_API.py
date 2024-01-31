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
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)
    employee_id = argv[1]
    if not employee_id.replace(".", "", 1).isdigit():
        print("Error: Employee ID must be a valid integer.")
        exit(1)
    employee_id = int(argv[1])
    response = r.get(F'{REST_API_URL}/users/{employee_id}').json()
    task_request = r.get(F'{REST_API_URL}/todos').json()
    emp_name = response.get('name')
    tasks = list(filter(lambda x: x.get('userId') == employee_id,
                        task_request))
    completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
    print(F'Employee {emp_name} is done with tasks '
          F'({len(completed_tasks)}/{len(tasks)}):')
    if len(completed_tasks) > 0:
        for task in completed_tasks:
            print(F'\t {task.get("title")}')
