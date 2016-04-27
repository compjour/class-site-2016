from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def homepage():
    somenumbers = range(1, 8)
    htmltxt = render_template('homepage.html',
                              the_date=datetime.now(),
                              numbers=somenumbers)
    return htmltxt

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
