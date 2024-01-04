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
    userName = r.json().get("username")

    params = {"userId": emp_id}
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/", params=params)

    with open(f"{emp_id}.json", "w", newline='') as f:
        todoList = r.json()
        todoDict = {}
        valueList = []
        for todo in todoList:
            element = {
                    "task": f"{todo.get('title')}",
                    "completed": todo.get('completed'),
                    "username": f"{userName}"
                    }
            valueList.append(element)

        todoDict[f"{emp_id}"] = valueList
        json.dump(todoDict, f)


if __name__ == "__main__":
    """if len(sys.argv) < 2:
        sys.exit()"""

    emp_id = sys.argv[1]

    """if type(eval(emp_id)) != int:
        sys.exit()"""

    retrieve_todo(emp_id)
