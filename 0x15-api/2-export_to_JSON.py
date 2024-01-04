#!/usr/bin/python3
"""
script requests todo list of given employee
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])
    u = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    t = requests.get(f"https://jsonplaceholder.typicode.com/todos")

    if u.status_code == 200 and t.status_code == 200:
        user_data = u.json()
        todo_data = t.json()
    else:
        print("URL REQUEST FAILED")

    selected_sets = [s for s in todo_data if s['userId'] == user_id]
    tasks = []
    for selected in selected_sets:
        task = {
            "task": selected["title"],
            "completed": bool(selected["completed"]),
            "username": user_data["username"]
        }
        tasks.append(task)

    user_tasks = {str(user_id): tasks}

    with open(f'{user_id}.json', 'w') as jsnf:
        json.dump(user_tasks, jsnf)
