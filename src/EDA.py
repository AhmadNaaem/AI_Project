import pandas as pd
import numpy as np
import seaborn as sns

def EDA(a):
    ch_data = a.drop(columns=['math score', 'reading score', 'writing score'])
    print(ch_data.head())
    print(ch_data.info())
    print(ch_data.nunique())
    
