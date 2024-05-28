#!python3
# vsearch_webapp5.py - Same as file vsearch_webapp4.py except
#                      added a function `render_search_response()`,


from vsearch import search_for_letters
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

def render_search_response(gen_json: bool=False) -> str:
    """Return either a JSON- or HTML-formatted search response."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letter))
    if gen_json:
        return jsonify(the_phrase=phrase,
                       the_letters=letters,
                       the_results=results)
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


@app.route('/search_for', methods=['POST'])
def search_for() -> 'html':
    """Returns the results of a call to 'search_for_letters' to the browser."""
    return render_search_response()


@app.route('/entryjson')
def entry_json_page() -> 'html':
    """Returns the JSON entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search_for_letters JSON page',
                           the_url='/searchjson')


@app.route('/searchjson', methods=['POST'])
def search_for_json() -> 'json':
    """Returns the results of a call to 'search_for_letters' to the browser."""
    return render_search_response(True)


if __name__ == '__main__':
    app.run(debug=True)
