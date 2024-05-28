#!python3
# vsearch_webapp3.py - Same as file vsearch_webapp2.py except
#                      search_for function values are not hardcoded
#                      instead received from the form, also added
#                      new decorator, `/search_for_json`


from flask import Flask, render_template, request, jsonify
from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to the browser."""
    return render_template('entry.html',
                           the_title='Welcome to search_for_letters on' +
                           ' the web!')


@app.route('/search_for', methods=['POST'])
def search_for() -> 'html':
    """Returns the results of a call to 'search_for_letters' to the browser."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    return render_template('results.html',
                           the_title='Here are your results!',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/search_for_json', methods=['POST'])
def search_for_json() -> 'json':
    """Returns the results of a call to 'search_for_letters' as json."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    return jsonify(the_phrase=phrase,
                   the_letters=letters,
                   the_results=results)

app.run(debug=True)