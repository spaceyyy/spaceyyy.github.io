#!python3
# vsearch_webapp.py - Flask framework w/ decorator and debugger


from flask import Flask
from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/search_for')
def search_for() -> str:
    """Returns the results of a call to 'search_for_letters' to the browser."""
    return str(search_for_letters('life, the univeser, and everything', 'xyz'))

app.run(debug=True)
