import numpy as np

def featureEng(df):
    #Percentage 
    df['percentage'] = ((df['math score'] + df['reading score'] + df['writing score']) / 300)*100
    
    # Grade
    df['grade'] = np.where(df['percentage'] >= 85, 'A',
    np.where(df['percentage'] >= 75, 'B',
    np.where(df['percentage'] >= 60, 'C',
    np.where(df['percentage'] >= 50, 'D', 'F'))))
    
    # Age
    df['age_group'] = np.where(df['age'] < 20, 'Below 20',
    np.where(df['age'] > 20, 'Above 20','20 yrs'))
    
    # IELTS
    i_mean = df['IELTS'].mean()
    df['ielts_group'] = np.where(df['IELTS'] > i_mean, 'Above 7',
    np.where(df['IELTS'] < i_mean, 'Below 7', '7'))
    
    return df
    