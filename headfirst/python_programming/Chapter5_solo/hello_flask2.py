#!python3
# hello_flask2.py - A program that uses the Flask framework to
#                   create a basic Flask webapp that displays string.
#                   Added second URL '/search_for' which returns
#                   calling the function w/ hardcoded values


from flask import Flask
from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search_for')
def do_search() -> str:
    return str(search_for_letters('life, the universe, and everything',
                                  'eiru,!'))


app.run()