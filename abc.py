import pickle
from pathlib import Path
root = Path(".")
RFmodel = pickle.load(open(root/"LoanPredictionMLImplementation"/"RFmodel.pkl","rb"))
