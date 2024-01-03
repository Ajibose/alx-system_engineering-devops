#!/usr/bin/python3
"""
    Retrieve data from API
"""
import json
import requests


def retrieve_todo(emp_id):
    """Retrive the todo list for a user"""
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{emp_id}")
    emp_name = r.json().get("name")

    params = {"userId": emp_id}
    r = requests.get(
            f"https://jsonplaceholder.typicode.com/todos/", params=params)

    todo_list = r.json()
    totalTasks = len(todo_list)
    completedList = []
    for todo in todo_list:
        if todo['completed'] is True:
            completedList.append(todo.get("title"))
    completedTask = len(completedList)

    print("Employee {} is done with tasks({}/{}):\n\t"
           .format( emp_name, completedTask, totalTasks),
            "\n\t ".join(completedList)) 

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        sys.exit()

    emp_id = sys.argv[1]

    if type(eval(emp_id)) != int:
        sys.exit()

    retrieve_todo(emp_id)
