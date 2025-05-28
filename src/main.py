from EDA import EDA 
from naiveBayes import train_model
from featureEngineering import featureEng 
import pandas as pd
import numpy as np


def main():
    data= pd.read_csv('src/visa_eligible.csv')
    n_data=featureEng(data)  
    ch_data,lb=EDA(n_data)
    train_model(ch_data,lb)

if __name__ == "__main__":
    main()