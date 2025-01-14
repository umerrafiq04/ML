#building url dynamically
# variable rule
# jinja  template engine
# info ----> pass to html page
'''
{{}} expressions to print output in html
{%...%}  conditions,for loops
{#...#}  comments
'''

# #4 verbs: get vs post......... put and delete
from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this website"


#1) variable rule
# @app.route("/success/<score>")
@app.route("/success/<int:score>") 
def success(score):
    # return f"your score is {score}"
    res=""
    if score>=50:
        res="passed"
    else:
        res="failed"    #pass this value to html page
    return render_template("result.html",results=res)

#2) 
@app.route("/successres/<int:score>") 
def successres(score):
    # return f"your score is {score}"
    res=""
    if score>=50:
        res="passed"
    else:
        res="failed"    #pass this value to html page
    exp={'score':score,'res':res}
    return render_template("result1.html",results=exp)
  

#3) if condition in html
@app.route("/successif/<int:score>") 
def successif(score):
    res=""
    return render_template("result2.html",results=score)
  
#4) dynamic url
@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":

        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        ds=float(request.form['datascience'])
        total_score=(science+maths+c+ds)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))
    
    # it will go to successres route and calculate pass or fail result





if __name__ == "__main__":
    app.run(debug=True)
