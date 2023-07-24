#!/usr/bin/python3

'''
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

import json
import requests
import sys


def call():
    """ function that carry out the activity"""

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    all_users = response.json()
    dictionary = {}
    for user in all_users:
        ID = user.get("id")
        Name = user.get("username")
        tasks = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
        tasks = tasks + '/todos/'
        tasks = requests.get(tasks).json()
        dictionary[ID] = []
        for task in tasks:
            new_dic = {"task": task.get('title'),
                       "completed": task.get('completed'),
                       "username": Name}
            dictionary[ID].append(new_dic)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)


if __name__ == '__main__':
    call()
