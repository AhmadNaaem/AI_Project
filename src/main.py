import EDA
import pandas as pd
import numpy as np

def main():
    data= pd.read_csv('Student Visa Dataset.csv')
    EDA.EDA(data)