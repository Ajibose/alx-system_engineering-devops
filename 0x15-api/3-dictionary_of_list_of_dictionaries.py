#!/usr/bin/python3
"""
    Retrieve data from API
"""
import json
import requests
import sys


def retrieve_todo():
    """Retrive the todo list for a user"""
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/users")
    usersDict = {}
    content = r.json()
    for user in content:
        usersDict[f"{user.get('id')}"] = user.get('username')
    # print(usersDict)

    r = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/")

    allTasks = {}
    for userId in usersDict.keys():
        allTasks[f"{userId}"] = []

    with open(f"todo_all_employees.json", "w", newline='') as f:
        todos = r.json()
        for todo in todos:
            userId = todo.get('userId')
            allTasks[
                    f"{userId}"].append({
                        "username": f"{usersDict[f'{userId}']}",
                        "task": f"{todo.get('title')}",
                        "completed": todo.get('completed')
                        })
        json.dump(allTasks, f)


if __name__ == "__main__":
    """if len(sys.argv) < 2:
        sys.exit()"""

    # emp_id = sys.argv[1]

    """if type(eval(emp_id)) != int:
        sys.exit()"""

    retrieve_todo()
