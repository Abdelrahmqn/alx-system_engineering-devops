#!/usr/bin/python3
"""
    module Documentation (urllib module)
    this file contain the implementation
    all employees with tasks owned of with specific id
"""


if __name__ == "__main__":
    """ok ok in alphabatical"""

    import requests
    from sys import argv as a
    import json

    # accessing the id of employees.
    emp_id = "https://jsonplaceholder.typicode.com/users"
    information = requests.get(emp_id)
    if information.status_code != 200:
        exit(1)
    info_js = information.json()

    # accessing the tasks completed or not completed for employees.
    emp_tasks = "https://jsonplaceholder.typicode.com/todos"
    tasks = requests.get(emp_tasks)
    if tasks.status_code != 200:
        exit(1)

    tasks_js = tasks.json()

    # {"task": "distinctio vitae autem nihil ut molestias quo",
    # "completed": true, "username": "Antonette"}
    filename = "todo_all_employees.json"

    all_emps = {}
    for i in info_js:
        user_id = i['id']
        username = i['username']
        all_emps[user_id] = []

        for task in tasks_js:
            if task["userId"] == user_id:
                all_emps[user_id].append({
                                "username": username,
                                "task": task['title'],
                                "completed": task['completed']
                                })

    with open(filename, "w") as js_file:
        json.dump(all_emps, js_file)
