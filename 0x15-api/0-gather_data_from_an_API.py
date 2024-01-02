#!/usr/bin/python3
"""
    Retrieve data from API
"""
import requests
import json


def retrieve_todo(emp_id):
    """Retrive the todo list for a user"""
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/users/",
            params={'id': emp_id})
    content = r.json()
    emp_name = content[0]['name']

    r = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/",
            params={'userId': emp_id})
    total_size = len(r.json())
    params = {'userId': emp_id, 'completed': 'true'}

    r = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/", params=params)
    todo_list = r.json()
    completed_size = len(todo_list)
    print(
            f"Employee {emp_name} is done with "
            f"tasks({completed_size}/{total_size}):"
            )

    for i in todo_list:
        print(f"\t {i['title']}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        sys.exit()

    emp_id = sys.argv[1]

    if type(eval(emp_id)) != int:
        sys.exit()

    retrieve_todo(emp_id)
