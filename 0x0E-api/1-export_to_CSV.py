#!/usr/bin/python3
"""
Gathering data from api and exporting to CSV
"""

import csv
import requests
from sys import argv


def taskstoCSV(employeeID):
    """
    Gathering data from api and exporting to CSV
    """
    username = ''
    alltodo = []

    empReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeID))
    todoReq = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employeeID))

    username = empReq.json().get('username')
    todoJSON = todoReq.json()

    for task in todoJSON:
        todoRow = []
        todoRow.append(employeeID)
        todoRow.append(username)
        todoRow.append(task.get('completed'))
        todoRow.append(task.get('title'))
        alltodo.append(todoRow)

    with open('{}.csv'.format(employeeID), 'w') as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvWriter.writerows(alltodo)

    return 0

if __name__ == '__main__':
    taskstoCSV(argv[1])
