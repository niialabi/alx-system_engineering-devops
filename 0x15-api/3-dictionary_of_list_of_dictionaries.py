#!/usr/bin/python3
"""
script requests todo list of given employee
"""

import json
import requests

if __name__ == "__main__":
    all_user_tasks = {}

    for user_id in range(1, 11):
        u = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}")
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

        all_user_tasks[str(user_id)] = tasks

    with open('todo_all_employees.json', 'w') as jsnf:
        json.dump(all_user_tasks, jsnf)
