import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# import pandas_profiling

def EDA(a):
    ch_data = a.drop(columns=['math score', 'reading score', 'writing score']) #dropping unnecessary columns
    
    
    print("\n",ch_data.head(),"\n") 
    print("\n",ch_data.info())       #showing the info of the data
    print("\n",ch_data.nunique())
    print("\n",ch_data.isnull().sum()) 
    
    ch_data= ch_data.drop_duplicates() #dropping duplicates
    
    print("\n",ch_data.describe()) #showing the description of the data
    
    temp = input("Do you want to see the distribution of the data? (y/n): ")
    if(temp == 'y' or temp == 'Y'):    
        for col in ch_data.select_dtypes(include=['object']).columns:
            plt.figure(figsize=(8,4))
            sns.countplot(x=col, data=ch_data)
            plt.title(f'Distribution of {col}')
            plt.show()
    
    label_encoders = {}
    for col in ch_data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        ch_data[col] = le.fit_transform(ch_data[col])
        label_encoders[col] = le

    plt.figure(figsize=(15,10))
    sns.heatmap(ch_data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.show()

    
    
    
    
    
    # for col in ch_data.select_dtypes(include=[np.number]).columns:
    #     plt.figure(figsize=(8,4))
    #     sns.histplot(ch_data[col], kde=True)
    #     plt.title(f'Distribution of {col}')
    #     plt.show()
    # ch_data.profile_report().to_file("EDA_report.html")
    
