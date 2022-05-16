#!/usr/bin/python3
"""
script that, using this REST API, for a given
employee ID, returns information about his/her todo list progress.
"""
import json
import requests

users = requests.get('https://jsonplaceholder.typicode.com/users/').json()

if __name__ == '__main__':
    params = {'completed': 'true'}
    tasksDictByUser = {}
    for i in range(1, len(users)+1):
        r = requests.get(
            'https://jsonplaceholder.typicode.com/users/?id={}'.format(i))
        r2 = requests.get(
            'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(i))
        r3 = requests.get(
            'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(i),
            params=params)
        userInfos = r.json()[0]
        userTasks = r2.json()
        doneTasks = r3.json()
        tasksList = []
        for task in userTasks:
            tasksDict = {}
            tasksDict["username"] = userInfos.get('username')
            tasksDict["task"] = task.get('title')
            tasksDict["completed"] = task.get('completed')
            tasksList.append(tasksDict)
        tasksDictByUser["{}".format(i)] = tasksList
    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(tasksDictByUser))
