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

    file_name = "{}.csv".format(id)

    with open(file_name, "a") as f:
        for todo in todos_js:
            completed = todo.get("completed")
            title = todo.get("title")
            csv_data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id,
                                                              emp_name,
                                                              completed,
                                                              title
                                                              )
            f.write(csv_data)


if __name__ == "__main__":
    tasks_done(sys.argv[1])
