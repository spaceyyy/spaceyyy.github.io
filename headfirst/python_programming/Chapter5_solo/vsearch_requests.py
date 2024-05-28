#!python3
# vsearch_requests.py - A program using the requests lib for an example


import requests

url = 'http://127.0.0.1:5000/search_for'

form_data = {'phrase': 'life, the universe, and everything',
             'letters': 'xyz'}

r = requests.post(url, data=form_data)

print(r.json())