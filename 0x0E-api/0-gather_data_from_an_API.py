#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
if __name__ == "__main__":

    import requests
    from sys import argv

    user_src = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    emp = requests.get(user_src).json()
    emp_name = emp.get('name')
    tasks_src = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        argv[1])
    comp_tasks = []
    all_tasks = requests.get(tasks_src).json()
    for task in all_tasks:
        if task.get('completed') is True:
            comp_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, len(comp_tasks), len(all_tasks)))

    if len(comp_tasks) > 0:
        for task in comp_tasks:
            print("\t {}".format(task))
