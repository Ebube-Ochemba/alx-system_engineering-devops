#!/usr/bin/python3
"""
This script fetches data from a REST API and displays the TODO list progress
for a given employee ID. The script accepts an integer as a parameter, which
is the employee ID, and displays the employee's TODO list progress in a
specific format.
It then exports the data in the JSON format.
"""

import json
import requests

if __name__ == '__main__':
    # URLs for fetching user and TODO data
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch data from the API
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Create a dictionary to hold the tasks data for all users
    all_tasks = {}

    # Iterate over each user and populate their tasks
    for user in users:
        user_id = user['id']
        user_name = user['username']

        # Filter tasks for the current user
        user_tasks = [
            {
                "username": user_name,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos if task['userId'] == user_id
        ]

        # Add the user's tasks to the dictionary
        all_tasks[user_id] = user_tasks

    # Create the JSON file with the data for all users
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(all_tasks, file)

    print(f"Data exported to {filename}")
