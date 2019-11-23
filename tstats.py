import numpy as np
from scipy import stats
import pandas as pd


pats_results = pd.read_csv(r'vector_allOK.csv')

colsy = pats_results.columns[1:-1]

group2 = pats_results.loc[:9,:]
group3 = pats_results.loc[10:19,:]
group4 = pats_results.loc[20:29,:]

#print(group2['CrCH2_30'])

# t-statystyka dla grup 2 i 3
print("GRUPA 2 I 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for elem23 in colsy:
    a = group2[elem23]
    b = group3[elem23]
    t2, p2 = stats.ttest_ind(a,b)
    print(elem23)
    print("t = " + str(t2))
    print("p = " + str(p2))

# t-statystyka dla grup 2 i 4
print("GRUPA 2 I 4 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for elem24 in colsy:
    a = group2[elem24]
    b = group4[elem24]
    t2, p2 = stats.ttest_ind(a,b)
    print(elem24)
    print("t = " + str(t2))
    print("p = " + str(p2))

# t-statystyka dla grup 3 i 4
print("GRUPA 3 I 4 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
for elem34 in colsy:
    a = group3[elem34]
    b = group4[elem34]
    t2, p2 = stats.ttest_ind(a,b)
    print(elem34)
    print("t = " + str(t2))
    print("p = " + str(p2))