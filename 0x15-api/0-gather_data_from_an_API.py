#!/usr/bin/python3
"""
This script fetches data from a REST API and displays the TODO list progress
for a given employee ID. The script accepts an integer as a parameter, which
is the employee ID, and displays the employee's TODO list progress in a
specific format.
"""

import requests
from sys import argv

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(argv) != 2:
        print("Usage: ./script.py <employee_id>")
        exit(1)

    # Fetch users and todos data from the API
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Get the list of tasks for the given user ID
    user_id = argv[1]
    tasks = [task for task in todos if str(task['userId']) == user_id]
    done_tasks = [task for task in tasks if task['completed']]

    # Get the user's name
    user_name = ''
    for user in users:
        if user_id == str(user['id']):
            user_name = user['name']
            break

    # Display the progress of the TODO list
    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, len(done_tasks), len(tasks)))
    for task in done_tasks:
        print('\t {}'.format(task['title']))
