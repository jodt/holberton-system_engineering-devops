#!/usr/bin/python3
"""
script that, using this REST API, for a given
employee ID, returns information about his/her todo list progress.
"""
import csv
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
    for usertask in userTasks:
        taskByUser = []
        taskByUser.append(usertask.get('userId'))
        taskByUser.append(userInfos.get('username'))
        taskByUser.append(usertask.get('completed'))
        taskByUser.append(usertask.get('title'))
        tasksList.append(taskByUser)
    filename = "{}.csv".format(user)
    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(tasksList)
