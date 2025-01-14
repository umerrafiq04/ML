from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this website"
#u can make as many as routes as u want
@app.route("/index")
def index():
    return "Welcome to the inex page of my website"


if __name__ == "__main__":
    app.run(debug=True)

          