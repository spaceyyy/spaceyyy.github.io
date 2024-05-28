#!python3
# vsearch_webapp4.py - Same as file vsearch_webapp3.py except added a 
#                      decorator `'/entryjson'`, and dunder code at the bottom.


from flask import Flask, render_template, request, jsonify
from vsearch import search_for_letters

app = Flask(__name__)


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


@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to the browser."""
    return render_template('entry.html',
                           the_title='Welcome to search_for_letters on' +
                           ' the web!', the_url='/search_for')


@app.route('/searchjson', methods=['POST'])
def search_for_json() -> 'json':
    """Returns the results of a call to 'search_for_letters' as json."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    return jsonify(the_phrase=phrase,
                   the_letters=letters,
                   the_results=results)


@app.route('/entryjson')
def entry_json_page() -> 'html':
    """Returns the JSON entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search_for_letters JSON page',
                           the_url='/searchjson')


if __name__ == '__main__':
    app.run(debug=True)
