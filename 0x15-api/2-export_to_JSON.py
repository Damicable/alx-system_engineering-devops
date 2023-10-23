#!/usr/bin/python3
"""Script to export employee's ID data to JSON formar."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
