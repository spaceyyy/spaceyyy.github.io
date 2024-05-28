#!python3
# hello_flask.py - A program that uses the Flask framework to 
#                  create a basic Flask webapp that displays string.


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


app.run()