import numpy as np

def featureEng(df):
    #Percentage 
    df['percentage'] = ((df['math score'] + df['reading score'] + df['writing score']) / 300)*100
    
    # Grade
    df['grade'] = np.where(df['percentage'] >= 90, 'A+',
                np.where(df['percentage'] >= 85, 'A',
                np.where(df['percentage'] >= 80, 'A-',
                np.where(df['percentage'] >= 75, 'B+',
                np.where(df['percentage'] >= 70, 'B',
                np.where(df['percentage'] >= 65, 'B-',
                np.where(df['percentage'] >= 60, 'C+',
                np.where(df['percentage'] >= 55, 'C',
                np.where(df['percentage'] >= 50, 'C-','F')))))))))
    
    # Age
    df['age_group'] = np.where(df['age'] < 18, 'Below 18',
                    np.where(df['age'] < 20, '18-19',
                    np.where(df['age'] < 22, '20-21',
                    np.where(df['age'] < 24, '22-23', '24 and above'))))

    # IELTS
    df['ielts_group'] = np.where(df['IELTS'] < 6, 'Below 6',
                        np.where(df['IELTS'] < 7, '6-6.9',
                        np.where(df['IELTS'] < 8, '7-7.9', '8 and above')))
    
    edu_order = {
        "some high school": 0,
        "high school": 1,
        "some college": 2,
        "associate's degree": 3,
        "bachelor's degree": 4,
        "master's degree": 5
    }
    df['parental_education_ord'] = df['parental level of education'].map(edu_order)
    
    
    return df
    