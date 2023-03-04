import pickle
from flask import Flask,request ,app,jsonify,url_for,render_template
from flask_cors import CORS
import numpy as np
import pandas as pd
from feature_engineering import FeatureEngineering

app = Flask(__name__)
CORS(app)
# Load the model
rf_model = pickle.load(open("RFmodel.pkl","rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods = ['POST'])
def predict_api():

    data = request.json['data']
    print("data before fe ",data)
    #feature engineering for the unknown data
    fe = FeatureEngineering()
    data = fe.feature_engineering(data)
    print("data after fe ",data)
    # convert data to array to feed to algorithm for predictions
    data = np.array([value for value in data.values()])
    # reshape the array as there is single row
    data = data.reshape(1, -1)
    output = rf_model.predict(data)[0]
    if output == 0:
        return "No"
    else :
        return "Yes"

@app.route("/predict",methods = ["POST"])    
def predict():
    data = {item[0]:item[1] for item in request.form.items()}
    #we are capturing rupees so lets convert to EGP
    data['ApplicantIncome'] = float(data['ApplicantIncome'])*0.3623
    data['CoapplicantIncome'] = float(data['CoapplicantIncome'])*0.3623
    print("***",data['ApplicantIncome'])
    print("***",data['CoapplicantIncome'])
    print(data)
    fe = FeatureEngineering()
    data = fe.required_format(data)
    print(data)
    data = fe.feature_engineering(data)
    print(data)
    # convert data to array to feed to algorithm for predictions
    data = np.array([value for value in data.values()])
    # reshape the array as there is single row
    data = data.reshape(1, -1)
    output = rf_model.predict(data)[0]
    if output == 0:
        return render_template("output.html",value = 0,prediction_text="Loan will not be approved")
    else :
        return render_template("output.html",value = 1,prediction_text="Loan will  be approved")


if __name__=="__main__":
    app.run(debug = True)
