#!/usr/bin/python3
"""
Gets a to-do list for a given id
"""
import json
import requests
import sys


def tasks_done():
    '''
    Script that displays an employee completed tasks
    Parameters:
    employee_id: Is an interger representing an employee id.
    '''

    id = 1
    all_tasks_dict = {}

    while True:
        url = "https://jsonplaceholder.typicode.com/users?id={}".format(id)
        res = requests.get(url)
        res_js = res.json()
        if len(res_js) == 0:
            break
        emp_name = res_js[0].get("username")

        url = "https://jsonplaceholder.typicode.com/todos"
        todos = requests.get(url)
        todos_js = todos.json()
        tasks_list = []

        for task in todos_js:
            if task.get("userId") == int(id):
                task_dict = {}
                task_dict["username"] = emp_name
                task_dict["task"] = task.get("title")
                task_dict["completed"] = task.get("completed")
                tasks_list.append(task_dict)

        all_tasks_dict[id] = tasks_list
        id += 1

    file_name = "todo_all_employees.json"
    with open(file_name, "a") as f:
        json.dump(all_tasks_dict, f)


if __name__ == "__main__":
    tasks_done()
