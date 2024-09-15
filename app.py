from flask import Flask, render_template, url_for, request
import pickle as p
import pickle
from flask import Flask, request,jsonify,render_template
import numpy as np
import pandas as pd

modelfile = 'models/final_prediction.pickle'
model = p.load(open(modelfile, 'rb'))
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/predict', methods =['GET','POST'])
def predict():
    Region = float(request.form['Region'])
    Fresh = float(request.form['Fresh'])
    Milk = float(request.form['Milk'])
    Grocery = float(request.form['Grocery'])
    Frozen = float(request.form['Frozen'])
    Detergents_Paper = float(request.form['Detergents_Paper'])
    Delicassen = float(request.form['Delicassen'])
    
    total = [[Region,Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen]]
    prediction = model.predict(total)
    prediction = int(prediction[0])
    
    
    if prediction==1:
        return render_template('index.html',predict="Customer belongs to Cluster Label 1")
    else:
        return render_template('index.html',predict="Customer belongs to Cluster Label 2")
    
if __name__ == "__main__":
    app.run(debug=True)