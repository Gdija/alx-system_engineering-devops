#!/usr/bin/python3
"""export to json file of list of dict"""
import json
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    res_user = requests.get('{}/users'.format(api_url))
    users = res_user.json()
    data = {}
    for user in users:
        res_list = []
        data[user.get('id')] = res_list
        res_todo = requests.get('{}/todos?userId={}'.format(
            api_url,
            user.get('id')))

        response = res_todo.json()
        for line in response:
            res_list.append({
                "username": user.get('username'),
                "task": line.get('title'),
                "completed": line.get('completed')})
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
