#!/usr/bin/python3
'''A script that gathers data from an API and exports it to a JSON file.
'''
import json
import requests


API_URL = 'https://jsonplaceholder.typicode.com'
"""
The URL of the JSONPlaceholder API.
"""


if __name__ == '__main__':
    # Make an API call to get users data
    users_res = requests.get('{}/users'.format(API_URL)).json()
    # Make an API call to get todos data
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    # Initialize a dictionary to store users' data
    users_data = {}

    # Iterate through each user
    for user in users_res:
        # Extract user ID and username
        id = user.get('id')
        user_name = user.get('username')
        # Filter todos associated with the user
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        # Prepare user's data
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        # Store user's data in the dictionary
        users_data['{}'.format(id)] = user_data

    # Write the JSON data to a file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
