#!/usr/bin/python3
"""
Gets a to-do list for a given id
"""
import requests
import sys


def tasks_done(id):
    '''
    Script that exports an employee completed into a csv
    Parameters:
    id: Is an interger representing an employee id.
    '''

    url = "https://jsonplaceholder.typicode.com/users?id={}".format(id)
    res = requests.get(url)
    res_js = res.json()
    emp_name = res_js[0].get("username")

    url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url)
    todos_js = todos.json()

    file_name = "{}.csv".format(id)

    with open(file_name, "a") as f:
        for todo in todos_js:
            if todo.get("userId") == int(id):
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
