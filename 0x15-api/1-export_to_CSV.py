#!/usr/bin/python3
"""export a csv file"""

import csv
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    res_user = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_username = res_user.json().get('username')
    res_todo = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    response = res_todo.json()
    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
# writer.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])
        for task in response:
            writer.writerow([
                employee_id,
                employee_username,
                task.get('completed'),
                task.get('title')
            ])
