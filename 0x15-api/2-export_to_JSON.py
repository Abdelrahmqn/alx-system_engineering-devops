#!/usr/bin/python3
"""
    module Documentation (urllib module)
    this file contain the implementation
    employee with tasks him/she owned of with specific id
"""


if __name__ == "__main__":
    import requests
    from sys import argv as a
    import json

    if len(a) != 2:
        exit(1)

    id_e = a[1]

    # accessing the id of employees.
    emp_id = f"https://jsonplaceholder.typicode.com/users/{id_e}"
    information = requests.get(emp_id)
    if information.status_code != 200:
        exit(1)
    info_js = information.json()

    # accessing the tasks completed or not completed for employees.
    emp_tasks = f"https://jsonplaceholder.typicode.com/todos?userId={id_e}"
    tasks = requests.get(emp_tasks)
    if tasks.status_code != 200:
        exit(1)

    tasks_js = tasks.json()

    # {"task": "distinctio vitae autem nihil ut molestias quo",
    # "completed": true, "username": "Antonette"}
    filename = f"{id_e}.json"

    list_inf = []
    for task in tasks_js:
        list_inf.append({
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": info_js.get("username")
                        })
    dic = {f"{id_e}": list_inf}
    with open(filename, "w") as js_file:
        json.dump(dic, js_file)
