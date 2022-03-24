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
    tasksList = []
    tasksCounter = 0

    employeeReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    todoReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeID))

    name = employeeReq.json().get('name')
    todoJSON = todoReq.json()

    for task in todoJSON:
        if task.get('completed') is True:
            tasksCounter += 1
            tasksList.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(name,
          tasksCounter, len(todoJSON)))

    for title in tasksList:
        print('\t {}'.format(title))

    return 0

if __name__ == '__main__':
    employeeTasks(sys.argv[1])
