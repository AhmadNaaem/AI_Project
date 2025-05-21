from EDA import EDA 
import pandas as pd
import numpy as np


def main():
    data= pd.read_csv('src/visa_eligible.csv')
    EDA(data)

if __name__ == "__main__":
    main()