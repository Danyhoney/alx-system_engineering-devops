#!/usr/bin/python3
"""
This script is designed to gather data from a public API, specifically the
JSONPlaceholder API, and export the collected data to a JSON file for
further analysis or usage.
The script operates by taking a user ID as a command-line argument and
retrieves the user's information as well as their associated todos (tasks
from the JSONPlaceholder API. It then organizes this data in a structured
JSON format and writes it to a JSON file for future use.
"""

import json  # Import the JSON module for working with JSON data
import re  # Import the regular expression module for pattern matching
import requests  # Import the requests module for making HTTP requests
import sys  # Import the sys module for system-specificparameters ane funcs

# The base URL of the JSONPlaceholder API
API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """
    Check if command line arguments were provided and proceed accordingly.
    """
    if len(sys.argv) > 1:
        """
        Check if the provided argument is a valid user ID (numerical).
        """
        if re.fullmatch(r'\d+', sys.argv[1]):
            """
            Extract the user ID and convert it to an integer.
            """
            id = int(sys.argv[1])

            """
            Make an API call to retrieve user information based
            on the provided user ID.
            """
            user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()

            """
            Make another API call to retrieve todos (tasks)
            associated with the user.
            """
            todos_res = requests.get('{}/todos'.format(API_URL)).json()

            """
            Extract the username of the user from the response.
            """
            user_name = user_res.get('username')

            # Filter todos for the given user
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            # Write the data to a JSON file
            with open('{}.json'.format(id), 'w') as file:
                """
                Map todos to the desired JSON format for better organization.
                """
                user_name = user_res.get('username')

            # Filter todos for the given user
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))

            # Write the data to a JSON file
            with open('{}.json'.format(id), 'w') as file:
                """
                Map todos to the desired JSON format for better organization.
                """
                user_data = list(map(
                    lambda x: {
                        'task': x.get('title'),
                        'completed': x.get('completed'),
                        'username': user_name
                    },
                    todos
                ))
                users_data = {
                    '{}'.format(id): user_data
                }

                """
                Write the structured JSON data to the file.
                """
                json.dump(users_data, file, indent=4)
