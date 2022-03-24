#!/usr/bin/python3
"""for a given employee ID, returns info about his/her TODO list progress"""
def get_todo():
    import requests
    from sys import argv
    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()

    task_list = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()

    completedTask = []

    for task in task_list:
        if task.get("completed") is True:
            completedTask.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completedTask), len(task_list)))
    for task in completedTask:
        print("\t {}".format(task))


if __name__ == '__main__':
    get_todo()
