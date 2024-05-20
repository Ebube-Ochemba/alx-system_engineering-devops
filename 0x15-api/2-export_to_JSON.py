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
from sys import argv

if __name__ == '__main__':
    # Check if the script is called with the correct number of arguments
    if len(argv) != 2:
        print("Usage: ./script.py <employee_id>")
        exit(1)

    user_id = argv[1]

    # URLs for fetching user and TODO data
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch data from the API
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Filter tasks for the given user ID
    tasks = [task for task in todos if str(task['userId']) == user_id]

    # Find the user's name
    user_name = ''
    for user in users:
        if user_id == str(user['id']):
            user_name = user['username']
            break

    # Create a dictionary to hold the task data
    user_tasks = {
        user_id: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
            }
            for task in tasks
        ]
    }

    # Create a JSON file with the user ID as the filename
    filename = f"{user_id}.json"

    # Write the data to the JSON file
    with open(filename, mode='w') as file:
        json.dump(user_tasks, file)

    print(f"Data exported to {filename}")
