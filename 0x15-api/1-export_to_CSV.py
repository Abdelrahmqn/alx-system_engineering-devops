#!/usr/bin/python3
"""module Documentation (urllib module)"""


if __name__ == "__main__":
    import requests
    from sys import argv as a
    import csv

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

    # "2","Antonette","False","repudiandae totam in est sint facere fuga"
    filename = f"{id_e}.csv"

    csv.register_dialect('myDialect',
                         delimiter=',',
                         quoting=csv.QUOTE_ALL)

    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, dialect='myDialect')
        for task in tasks_js:
            writer.writerow([id_e, info_js.get('username'),
                             task.get('completed'),
                             task.get('title')])
