

#  Handling outliers :- it is important to remove outliers because it impacts the model performance.
"""Number summary
1 Min values
2. Q1 - 25 percentile
3. Median
4. Q3 - 75 percentile
5. Maximum """

import numpy as np

# lst_marks=[45,32,56,75,89,54,32,89,90,87,67,54,45,98,99,67,74]

# np.percentile(lst_marks,[25])

# we define a range )lower_fence and higher_fence and the number lower than lower_fence and number higher then the higher_fence 
# are called outliers in the data set.
"""
to caluculate lower_fence and higher_fence we need to calculate minimum,Q1,median,Q3,Maximum
minimum = np.percentile(lst_marks,[0])
q1 (25%) = np.percentile(lst_marks,[25])
median = np.percentile(lst_marks,[50])
q3 = np.percentile(lst_marks,[75])
maximum = np.percentile(lst_marks,[100])
"""
# we can do this even using a function ex :-

# minimum,Q1,median,Q3,maximum = np.quantile(lst_marks,[0,0.25,0.50,0.75,1.0])

# print(minimum,Q1,median,Q3,maximum)

"""
To calculate lower_fence and higher_fence we use this formula..
IQR = Interquartile range (is measure of statistical dispersion, which is spread of the data). It is defined as 
the difference between 75th and 25th percetiles of the data.
IQR = (Q3-Q1)
lower_fence = Q1 - 1.5(IQR)
higher_fence = Q3 + 1.5(IQR)
"""

# IQR = Q3-Q1

# lower_fence = Q1 - 1.5*(IQR)
# higher_fence = Q1 + 1.5*(IQR)

# print(lower_fence,higher_fence)

# calulating outliers in the datasets..

def Calc_Outliers(lst_marks):
    minimum,Q1,median,Q3,maximum = np.quantile(lst_marks,[0.0,0.25,0.50,0.75,1.0])
    IQR = Q3-Q1
    lower_fence = Q1 - 1.5*(IQR)
    higher_fence = Q1 + 1.5*(IQR)
    outliers = []
    for ele in lst_marks:
        if ele < lower_fence or ele > higher_fence :
            outliers.append(ele)
    
    return outliers

# print(Calc_Outliers(lst_marks=[12,23,12,1000,768,123,-123,-10,-200,-250,-560]))

lst_marks=[12,23,12,1000,768,123,-123,-10,-200,-250,-560]

# we can use boxpot to find outliers in the dataset the dots in the graph indicates outliers.
import seaborn as sns
import matplotlib.pyplot as plt

# sns.boxplot(lst_marks)
# plt.show()









