#!/usr/bin/python3
"""module Documentation (urllib module)"""


if __name__ == "__main__":
    import requests
    from sys import argv as a

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

    tsk_completed = [task for task in tasks_js if task.get("completed")]
    length_of_completed_tsks = len(tsk_completed)

    print("Employee {} is done with tasks({}/{}):"
          .format(info_js.get("name"),
                  length_of_completed_tsks, len(tasks_js)))
    for task in tsk_completed:
        print(f"\t {task.get('title')}")
