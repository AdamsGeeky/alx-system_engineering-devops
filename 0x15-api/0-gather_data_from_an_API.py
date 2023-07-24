#!/usr/bin/python3

'''
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

import requests
import sys


def call():
    """ function that carry out the activity"""
    Id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + Id

    response = requests.get(url)
    Name = response.json().get('name')

    todo = url + "/todos"
    tasks = requests.get(todo).json()
    done = 0
    completed = []

    for task in tasks:
        if task.get('completed'):
            completed.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(Name, done, len(tasks)))

    for task in completed:
        print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    call()
