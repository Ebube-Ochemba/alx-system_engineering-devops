#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos data
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get("completed")]
    num_done_tasks = len(done_tasks)

    # Print the output
    print(
        f"Employee {employee_name} is done with tasks"
        f"({num_done_tasks}/{total_tasks}):"
        )
    for task in done_tasks:
        print(f"\t {task.get('title')}")
