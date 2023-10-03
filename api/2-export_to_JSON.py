"""
This script fetches employee data and exports it in JSON format.
It records all tasks owned by the specified employee.

Usage: python export_to_JSON.py <employee_id>
"""

import requests
import sys
import json

def get_employee_data(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a request to get employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Make a request to get the TODO list for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()

    if not todos_data:
        print(f"No tasks found for Employee {username} (ID: {user_id}).")
        return

    # Create a dictionary to store the tasks in JSON format
    task_dict = {str(user_id): []}
    for task in todos_data:
        task_completed = task["completed"]
        task_title = task["title"]
        task_dict[str(user_id)].append({"task": task_title, "completed": task_completed, "username": username})

    # Create a JSON file for the employee
    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(task_dict, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_data(employee_id)