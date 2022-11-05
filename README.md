# LoanApprovalPrediction

## SOFTWARE AND TOOLS REQUIRED:

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment

    conda create -p LoanApprovalEnv python==3.7 -y

sample data for o/p "yes":
{
   "data": {
      "Loan_ID": "LP001015",
      "Gender": "Male",
      "Married": "Yes",
      "Dependents": "0",
      "Education": "Graduate",
      "Self_Employed": "No",
      "ApplicantIncome": 5720,
      "CoapplicantIncome": 0,
      "LoanAmount": 110,
      "Loan_Amount_Term": 360,
      "Credit_History": 1,
      "Property_Area": "Urban"
   }
}
sample data for o/p "no":
{
   "data": {
      "Loan_ID": "LP001056",
      "Gender": "Male",
      "Married": "Yes",
      "Dependents": "2",
      "Education": "Not Graduate",
      "Self_Employed": "No",
      "ApplicantIncome": 3881,
      "CoapplicantIncome": 0,
      "LoanAmount": 147,
      "Loan_Amount_Term": 360,
      "Credit_History": 0,
      "Property_Area": "Rural"
   }
}