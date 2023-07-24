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
    Id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users" + "/" + Id

    response = requests.get(url)
    Name = response.json().get('username')

    todo = url + "/todos"
    tasks = requests.get(todo).json()

    dictionary = {Id: []}
    for task in tasks:
        new_dic = {"task": task.get('title'),
                   "completed": task.get('completed'),
                   "username": Name}
        dictionary[Id].append(new_dic)

    with open('{}.json'.format(Id), 'w') as file:
        json.dump(dictionary, file)


if __name__ == '__main__':
    call()
