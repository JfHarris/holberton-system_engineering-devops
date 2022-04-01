#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""

import csv
import requests
from sys import argv


def save_to_CSV(employeeID):
    """extend your Python script to export data in the CSV format"""
    name = ''
    allTasks = []

    empReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    tasksReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employeeID))

    name = empReq.json().get('username')
    taskJSON = tasksReq.json()

    for task in taskJSON:
        taskInfo = []
        taskInfo.append(employeeID)
        taskInfo.append(name)
        taskInfo.append(task.get('completed'))
        taskInfo.append(task.get('title'))
        allTasks.append(taskInfo)

    with open('{}.csv'.format(employeeID), 'w') as csvFile:
        csvInp = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvInp.writerows(allTasks)

    return 0


if __name__ == '__main__':
    save_to_CSV(argv[1])
