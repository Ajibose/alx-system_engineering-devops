#!/usr/bin/python3
"""
    Retrieve data from API
"""
import json
import requests
import sys


def retrieve_todo(emp_id):
    """Retrive the todo list for a user"""
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{emp_id}")
    emp_name = r.json().get("name")

    params = {"userId": emp_id}
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/", params=params)

    with open(f"{emp_id}.csv", "w", newline='') as f:
        todo_list = r.json()
        writer = csv.writer(f)
        for todo in todo_list:
            csvLine = f'"{emp_id}"' + f'"{emp_name}"' + f'"{todo.get("title")}"'
            writer.writerow(csvLine)


if __name__ == "__main__":
    """if len(sys.argv) < 2:
        sys.exit()"""

    emp_id = sys.argv[1]

    """if type(eval(emp_id)) != int:
        sys.exit()"""

    retrieve_todo(emp_id)
