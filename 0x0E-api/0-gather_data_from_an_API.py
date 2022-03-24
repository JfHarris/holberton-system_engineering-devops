#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""


import requests
import sys


def employeeTasks(employeeID):
    """
    for a given employee ID, returns information about TODO list progress
    """
    name = ''
    tasks = []
    tasksCounter = 0

    empReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    todoReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeID))

    name = empReq.json().get('name')
    todoJSON = todoReq.json()

    for task in todoJSON:
        if task.get('completed') is True:
            tasksCounter += 1
            tasks.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(name,
          tasksCounter, len(todoJSON)))

    for title in tasks:
        print('\t {}'.format(title))

if __name__ == '__main__':
    employeeTasks(sys.argv[1])
