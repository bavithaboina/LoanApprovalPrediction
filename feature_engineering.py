import pandas as pd
import numpy as np

train = pd.read_csv(r"Data/train.csv")
print(train["Gender"].head())

class FeatureEngineering():
    def __init__(self):
        pass

    def impute_missing(self,data):
        
        categorical_discrete_num = ["Gender","Married","Dependents","Education","Self_Employed","Property_Area","Loan_Amount_Term","Credit_History"]
        impute_mode = {}
        for feature in categorical_discrete_num:
            impute_mode[feature] = train[feature].mode()[0]
        #print(impute_mode)
        continuous_numerical = ["LoanAmount","ApplicantIncome","CoapplicantIncome"]
        impute_median = {}
        for feature in continuous_numerical:
            impute_median[feature] = train[feature].median()
        #print(impute_median)
        for feature in categorical_discrete_num:
            if feature not in data.keys():
                data[feature] = impute_mode[feature]
        for feature in continuous_numerical:
            if feature not in data.keys():
                data[feature] = impute_median[feature]
        return data

    def derived_features(self,data):
        #newly added features
        new_features = ['Balance_Income','Total_Income','EMI']
        data["Total_Income"] = data['ApplicantIncome']+data['CoapplicantIncome']
        data["EMI"] = data['LoanAmount']/data['Loan_Amount_Term'] 
        data['Balance_Income'] = data["Total_Income"]-(data["EMI"]*1000)
        return data

    def encode(self,data):
        encoded_features = ['Gender_Female', 'Gender_Male', 'Married_No', 'Married_Yes', 'Dependents_0', 'Dependents_1', 'Dependents_2', 'Dependents_3+', 'Education_Graduate', 'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes', 'Property_Area_Rural', 'Property_Area_Semiurban', 'Property_Area_Urban']
        categorical_features = ["Gender","Married","Dependents","Education","Self_Employed","Property_Area"]
        for cat_feat in categorical_features:
            data[cat_feat+"_"+str(data[cat_feat])]=1
        return data

    def log(self,data):
        log_features = ['LoanAmount']
        for log_feat in log_features:
            data[log_feat+"_log"]=np.log(data[log_feat])
        return data

    def rearrange(self,data):
        features = ['Credit_History', 'LoanAmount_log', 'Gender_Female', 'Gender_Male', 'Married_No', 'Married_Yes', 'Dependents_0', 'Dependents_1', 'Dependents_2', 'Dependents_3+', 'Education_Graduate', 'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes', 'Property_Area_Rural', 'Property_Area_Semiurban', 'Property_Area_Urban', 'Total_Income', 'Total_Income_log', 'EMI', 'Balance_Income']
        #print(features)
        data_for_model = {}
        for feature in features:
            if feature in data.keys():
                data_for_model[feature] = data[feature]
            else :
                data_for_model[feature] = 0
        return data_for_model

    def feature_engineering(self,data):
        data = self.impute_missing(data)
        data = self.derived_features(data)
        data = self.encode(data)
        data = self.log(data)
        data = self.rearrange(data)
        return data
    
    def required_format(self,data):
        numerical_features = ["LoanAmount","ApplicantIncome","CoapplicantIncome","Loan_Amount_Term","Credit_History"]
        for feature in data.keys():
            if feature in numerical_features:
                data[feature] = int(data[feature])
        return data