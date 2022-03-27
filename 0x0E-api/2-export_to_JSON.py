#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    user_add = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    emp = requests.get(user_add).json()
    emp_username = emp.get('username')

    tasks_add = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    all_tasks = requests.get(tasks_add).json()

    filename = "{}.json".format(argv[1])

    todo_dict = {}
    todo_tasks = []
    for task in all_tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = emp_username
        todo_tasks.append(task_dict)
        todo_dict[argv[1]] = todo_tasks
        json_string = json.dumps(todo_dict)

    with open(filename, 'w') as f:
        f.write(json_string)
