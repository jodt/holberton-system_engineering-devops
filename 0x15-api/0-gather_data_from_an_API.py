#!/usr/bin/python3
"""
script that, using this REST API, for a given
employee ID, returns information about his/her todo list progress.
"""
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
    numberoftasks = r2.json()
    doneTasks = r3.json()
    print('Employee {} is done with tasks ({}/{}):'.format(
        userInfos.get('name'), len(doneTasks), len(numberoftasks)))
    for task in doneTasks:
        print("\t {}".format(task.get('title')))
