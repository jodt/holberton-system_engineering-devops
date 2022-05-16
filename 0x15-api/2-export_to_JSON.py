#!/usr/bin/python3
"""
script that, using this REST API, for a given
employee ID, returns information about his/her todo list progress.
"""
import json
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    params = {'completed': 'true'}
    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/?id={}'.format(user))
    r2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(user))
    r3 = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(user),
        params=params)
    userInfos = r.json()[0]
    userTasks = r2.json()
    doneTasks = r3.json()
    tasksList = []
    for task in userTasks:
        tasksDict = {}
        tasksDict["task"] = task.get('title')
        tasksDict["completed"] = task.get('completed')
        tasksDict["username"] = userInfos.get('username')
        tasksList.append(tasksDict)
    tasksDictByUser = {"{}".format(user): tasksList}
    filename = "{}.json".format(user)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(tasksDictByUser))
