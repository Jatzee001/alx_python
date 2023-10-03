"""
This script fetches employee data and exports it in a JSON format.
It records all tasks from all employees and stores them in a JSON file.

Usage: python export_to_JSON.py
"""

import csv
import json
import requests

def get_all_employee_data():
    """
    Fetches employee data and exports it in JSON format.

    Args:
        None

    Returns:
        None
    """
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()

    # Create a dictionary to store all tasks from all employees
    all_employee_tasks = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        # Fetch tasks for each user
        todos_response = requests.get(f"{base_url}/users/{user_id}/todos")
        todos_data = todos_response.json()

        # Create a list to store the tasks as dictionaries
        tasks_list = []

        for task in todos_data:
            task_completed = task["completed"]
            task_title = task["title"]
            tasks_list.append({"username": username, "task": task_title, "completed": task_completed})

        # Add the list of tasks to the dictionary with user ID as the key
        all_employee_tasks[str(user_id)] = tasks_list

    # Create a JSON file for all employees
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employee_tasks, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    get_all_employee_data()