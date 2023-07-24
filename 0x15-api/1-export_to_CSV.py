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
    Name = response.json().get('username')

    todo = url + "/todos"
    tasks = requests.get(todo).json()
    done = 0
    completed = []

    with open('{}.csv'.format(Id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(Id, Name, task.get('completed'),
                               task.get('title')))


if __name__ == '__main__':
    call()
