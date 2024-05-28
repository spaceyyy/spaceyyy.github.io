#!python3
# vsearch_for_web.py - A program that uses the Flask framework to
#                      create a basic Flask webapp. Including multiple
#                      URLs and removing redirect in hello() function and
#                      adding the home URL `'/'` to redirect to `'/entry'`


from flask import Flask, render_template, request, jsonify
from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/search_for', methods=['POST'])
def do_search() -> 'html':
    """Returns the results of a call to 'search_for_letters' to the browser."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_letters(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search_for_letters on the' +
                           ' web!')


if __name__ == '__main__':
    app.run(debug=True)
