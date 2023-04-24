#!/usr/bin/python3
"""
Gets a to-do list for a given id
"""
import json
import requests
import sys


def tasks_done(id):
    '''
    Script that displays an employee completed tasks
    Parameters:
    employee_id: Is an interger representing an employee id.
    '''

    url = "https://jsonplaceholder.typicode.com/users?id={}".format(id)
    res = requests.get(url)
    res_js = res.json()
    emp_name = res_js[0].get("username")

    url = "https://jsonplaceholder.typicode.com/todos".format(id)
    todos = requests.get(url)
    todos_js = todos.json()
    tasks_list = []

    for task in todos_js:
        if task.get("userId") == int(id):
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = emp_name
            tasks_list.append(task_dict)

    todos = {str(id): tasks_list}
    file_name = str(id)+".json"

    with open(file_name, "a") as f:
        json.dump(todos, f)


if __name__ == "__main__":
    tasks_done(sys.argv[1])
