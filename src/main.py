from EDA import EDA 
from naiveBayes import train_model
import pandas as pd
import numpy as np


def main():
    data= pd.read_csv('src/visa_eligible.csv')
    ch_data,lb=EDA(data)
    train_model(ch_data,lb)

if __name__ == "__main__":
    main()