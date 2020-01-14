import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

# run the application
if __name__ == "__main__":
    app.run(debug=True)