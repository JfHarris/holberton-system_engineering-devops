#!/usr/bin/python3
"""using REST API, for employee ID, returns infn about TODO list progress. """

import requests
import sys

def empTasks(employeeID):
    """returns info about an employee"""
    name = ''
    tasksList = []
    tasksCounter = 0
    empReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    tasksReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeID))

    name = empReq.json().get('name')
    taskJSON = tasksReq.json()

    for task in taskJSON:
        if task.get('completed') is True:
            tasksCounter += 1
            tasksList.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(name,
          tasksCounter, len(taskJSON)))

    for title in tasksList:
        print('\t {}'.format(title))

    return 0

if __name__ == '__main__':
    empTasks(sys.argv[1])
