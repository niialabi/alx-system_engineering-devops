#!/usr/bin/python3
"""
script requests todo list of given employee
"""
import csv
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
    done = [d for d in selected_sets if d['completed'] is True]


    with open(f'{user_id}.csv', 'w', newline='') as csvf:
        csvwriter = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for selected in selected_sets:
            csvwriter.writerow([user_id, user_data['username'], selected['completed'], selected['title']])

    """
    done_count = done.__len__()
    todo_count = selected_sets.__len__()
    mid_s = "is done with tasks"
    s = f"Employee {user_data['name']} {mid_s}({done_count}/{todo_count}): "
    print(s)
    for selected in done:
        print("\t {}".format(selected['title']))

    ----------
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv    
    "2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
    """