#!/usr/bin/python3
"""export to json file"""
import json
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    res_user = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_username = res_user.json().get('username')
    res_todo = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    response = res_todo.json()
    with open('{}.json'.format(employee_id), 'w') as file:
        res_list = []
        data = {employee_id: res_list}
        for line in response:
            res_list.append({
                "task": line.get('title'),
                "completed": line.get('completed'),
                "username": employee_username
            })
        json.dump(data, file)
