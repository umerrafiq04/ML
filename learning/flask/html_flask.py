from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to the course</h1></html>"  #this is confusng ie y we prefer using another library clled render template
#u can make as many as routes as u want
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)