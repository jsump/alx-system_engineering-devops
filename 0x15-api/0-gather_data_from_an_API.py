#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API

This module is a script that uses a REST API for agiven employee ID,
returns informations ablout his/her TOTO list progress
"""


import requests


def get_employee_todo_list_progress(employee_id):
    """
    This function uses REST API to retrieve the employee TODO
    list progress.
    The script must accept an integer as a parameter, employee_id
    """
    url = f'https://jsonplaceholder.typicode.com/todos?userID={employee_id}'
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No TODO list found for employer ID given")

    employee_name = todos[0].get('username')
    if employee_name is None:
        print("No 'username' found for this employee")
        return

    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)

    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{total_tasks}):")
    employee_is = 1
    get_employee_todo_list_progress(employee_id)

    for task in completed_taks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = 2
    get_employee_todo_list_progress(employee_id)
