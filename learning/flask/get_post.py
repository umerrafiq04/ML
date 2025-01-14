#4 verbs: get vs post......... put and delete
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this website"
#u can make as many as routes as u want

# by default it will be get
@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the index page of my website"


@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f"hello {name}"
    return render_template("form.html")
    


if __name__ == "__main__":
    app.run(debug=True)

     