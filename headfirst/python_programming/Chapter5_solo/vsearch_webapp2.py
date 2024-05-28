#!python3
# vsearch_webapp2.py - Same as file vsearch_webapp.py plus
#                      an `/entry` URL added and render_template lib


from flask import Flask, render_template
from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/search_for')
def search_for() -> str:
    """Returns the results of a call to 'search_for_letters' to the browser."""
    return str(search_for_letters('life the universe, and everything', 'xyz'))


@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search_for_letters' +
                           ' on the web!')

app.run(debug=True)