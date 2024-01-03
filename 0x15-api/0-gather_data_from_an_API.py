#!/usr/bin/python3
""" script requests todo list of given employee """

import requests
from sys import argv

user_id = int(argv[1])
if __name__ == "__main__":
    u = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    t = requests.get(f"https://jsonplaceholder.typicode.com/todos")

    if u.status_code == 200 and t.status_code == 200:
        user_data = u.json()
        todo_data = t.json()
    else:
        print("URL REQUEST FAILED")

    selected_sets = [s for s in todo_data if s['userId'] == user_id]
    done = [d for d in selected_sets if d['completed'] is True]

    print(f"Employee {user_data['name']} is done with tasks(
        {done.__len__()}/{selected_sets.__len__()}): ")
    for selected in done:
        print(f"\t{selected['title']}")
