#!/usr/bin/python3
"""
This module fetches data from a REST API and displays the TODO list progress
for a given employee ID. It uses the requests module to make HTTP requests.

Usage:
    python3 script.py <employee_id>
"""

import requests
import sys


def fetch_user_data(employee_id):
    """
    Fetch user data for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: The user data as a dictionary.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    return user_response.json()


def fetch_todos_data(employee_id):
    """
    Fetch TODO list data for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of todos as dictionaries.
    """
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
    todos_response = requests.get(todos_url)
    return todos_response.json()


def display_todo_progress(employee_name, todos):
    """
    Display the TODO list progress for an employee.

    Args:
        employee_name (str): The name of the employee.
        todos (list): A list of todos as dictionaries.
    """
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]
    num_done_tasks = len(done_tasks)

    # Print the progress summary
    print(
        f"Employee {employee_name} is done with tasks"
        "({num_done_tasks}/{total_tasks}):"
        )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Fetch and process data
    user_data = fetch_user_data(employee_id)
    employee_name = user_data.get("name")
    todos = fetch_todos_data(employee_id)

    # Display the TODO list progress
    display_todo_progress(employee_name, todos)
