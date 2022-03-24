#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == '__main__':
    try:
        employ_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=employ_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    res = requests.get(user_uri).json()

    employ = res.get("name")

    res = requests.get(todo_uri).json()

    totes = len(res)

    no_task = sum([elem["completed"] is False for elem in res])

    comp = totes - no_task

    str = "Employee {name} is done with tasks({comp}/{totes}):"
    print(str.format(name=employ, comp=comp, totes=totes))

    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
