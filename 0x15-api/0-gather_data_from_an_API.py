#!/usr/bin/python3
"""
Gets a to-do list for a given id
"""
import requests
import sys


def tasks_done(id):
    '''
    Script that displays an employee completed tasks
    Parameters:
    employee_id: Is an interger representing an employee id.
    '''

    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    res = requests.get(url)
    res_js = res.json()
    emp_name = res_js.get("name")

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(url)
    todos_js = todos.json()
    no_of_tasks = len(todos_js)

    task_compleated = 0
    task_list = ""

    for task in todos_js:
        if task.get("completed") is True:
            task_compleated += 1
            task_list += "\t " + task.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(emp_name,
                                                          task_compleated,
                                                          no_of_tasks))
    print(task_list[:-1])


if __name__ == "__main__":
    tasks_done(sys.argv[1])
