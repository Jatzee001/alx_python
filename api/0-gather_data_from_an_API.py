import requests
import sys

def get_employee_data(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a request to get employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Make a request to get the TODO list for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos_data if todo["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Print the employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_data(employee_id)
