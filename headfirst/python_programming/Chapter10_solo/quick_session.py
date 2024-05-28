#!python3
# quick_session.py - A program showcasing the `session` library in use.
#                    When running this and opening a browser, the `<user>`
#                    code is where you type the name of the user in the URL


from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'


@app.route('/setuser/<user>')
def set_user(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def get_user() -> str:
    return 'User value is currently set to: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)
