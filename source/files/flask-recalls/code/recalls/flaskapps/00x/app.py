from flask import Flask
from settings import get_data
app = Flask(__name__)
data = get_data()

@app.route("/")
def homepage():
    return "The data includes %s things" % len(data)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
