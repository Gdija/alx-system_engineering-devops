#!/usr/bin/python3
""" returns information about user todo list progress"""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    res_user = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_name = res_user.json().get('name')
    res_todo = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    response = res_todo.json()

    done_task = [task for task in response if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, len(done_task), len(response)))

    for task in done_task:
        print('\t {}'.format(task.get('title')))
