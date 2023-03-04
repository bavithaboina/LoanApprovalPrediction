# LoanApprovalPrediction

## SOFTWARE AND TOOLS REQUIRED:

1. [Github Account](https://github.com)
2. [AWS Account](https://aws.amazon.com/console/)
3. [VS Code IDE](https://code.visualstudio.com/)


Steps for executing on the local system:

Step 1: Create a new environment

    conda create -p LoanApprovalEnv python==3.7 -y

Step 2 : navigate to the location of the downloaded file and activate the environment created

   conda activate LoanApprovalEnv

Step 3 : install the required packages

   pip install -r requirements.txt

Step 4: Run the code

   python app.py

## Steps I followed to  create a Machine Learning Model
1. Understand the problem statement
2. Hypothesis Generation (list out all the possible factors that can affect the outcome before looking at the data)
3. Have a look at the meaning of each feature provided
4. Exploratory Data Analysis ( EDA )
    * Understand the data
    * Perform univariate Analysis
    * Perform Bivariate Analysis
5. Feature Engineering(FE) Part 1 (depends on the data ,On the available data I have performed the following)
    * Handle missing values
    * Treat Outliers
    * Perform Encoding
6. Feature Engineering(FE) Part 2 (depends on the data ,On the available data I have performed the following)
    * create new features that can affect the target variable ( based on domain knowledge)
        * Total Income
        * EMI
        * Balance Income
7. Use different classification algorithms ,perform hyper parameter tuning and finalise the model based on the evaluation criteria(Here I have used accuracy)
8. Now you can pickle the model so that it can be used while creating a flask api
