from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this website"

@app.route("/fill",methods=["GET","POST"])
def fill():
         if request.method=="POST":
               name=request.form["num"]
         else:
            return render_template("form.html")
        #  return redirect(url_for('send',score=name))
         return render_template("form.html",results=name)

# @app.route("/send/<int:score>")
# def send(score):
#      return render_template("result1.html",results=score)
      


if __name__ == "__main__":
    app.run(debug=True)

          