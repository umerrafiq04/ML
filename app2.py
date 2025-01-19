from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
application=Flask(__name__)
app=application
# interact with pkl to do transformation(feature scaling) and predicition
# import ridege regressor and standard  scaler pickle
ridge_model=pickle.load(open("models/ridge.pkl","rb"))
standard_scaler=pickle.load(open("models/scaler.pkl","rb"))


@app.route("/")
def hello_world():
    return render_template("index.html")
if __name__ == "_main_":
    app.run(host="0.0.0.0")