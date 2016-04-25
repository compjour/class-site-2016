from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def homepage():
    tname = 'hello.html'
    return render_template(tname, the_date=datetime.now(), numbers=list(range(1,11)))

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
