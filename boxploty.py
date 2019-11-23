import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import io
import statistics as st
import math
import seaborn as sns

who_II30 = pd.read_csv(r'who_ii_30ms\results_csv\matrix_all_II30ms.csv', index_col = " ")
who_II135 = pd.read_csv(r'who_ii_135ms\results_csv\matrix_all_II135.csv', index_col = " ")
who_III30 = pd.read_csv(r'who_iii_30ms\results_csv\matrix_all_III30.csv', index_col = " ")
who_III135 = pd.read_csv(r'who_iii_135ms\results_csv\matrix_all_III135.csv', index_col = " ")
who_IV30 = pd.read_csv(r'who_iv_30 ms\results_csv\matrix_all_IV30.csv', index_col = " ")
who_IV135 = pd.read_csv(r'who_iv_135ms\results_csv\matrix_all_IV135.csv', index_col = " ")

metab_count = len(who_II30.iloc[1,:])

df1 = pd.DataFrame(who_II30.iloc[:,16]).assign(Grupa=2)
df2 = pd.DataFrame(who_III30.iloc[:,16]).assign(Grupa=3)
df3 = pd.DataFrame(who_IV30.iloc[:,16]).assign(Grupa=4)
cdf = pd.concat([df1, df2, df3])    
plt.figure(num = None, figsize=(6,9))
mdf = pd.melt(cdf, id_vars=['Grupa'])
ax = sns.boxplot(x="Grupa", y="value", data=mdf)
ax = sns.stripplot(x="Grupa", y="value", data=mdf,
                   jitter=True, 
                   marker='o', 
                   alpha=0.5,
                   color='black')
plt.title(str(who_II135.columns[16])+'_30')
plt.grid(True)

# for i in range(0, metab_count):
#     plt.figure(i)
#     who_II30[str(who_II135.columns[i])] = pd.Series(who_II30.iloc[:,i])
#     box30 = who_II30.boxplot(by = str(who_II135.columns[i]))
    # vals30 = pd.concat([who_II30.iloc[:,i],who_III30.iloc[:,i], who_IV30.iloc[:,i]], axis=1)
    # print(vals30)
    # values30 = {'2': [who_II30.iloc[:,i]], '3': [who_III30.iloc[:,i]], '4': [who_IV30.iloc[:,i]]}
    #val30_df = pd.DataFrame(vals30, columns = ['2', '3', '4'])
    # values135 = {'2': [who_II135.iloc[:,i]], '3': [who_III135.iloc[:,i]], '4': [who_IV135.iloc[:,i]]}
    # val135_df = pd.DataFrame(values135, columns = ['2', '3', '4'])
    #print(val30_df)
    #boxplot30 = vals30.boxplot(column = ['2', '3', '4'])
    # boxplot135 = val135_df.boxplot()
    # boxplot30.figure.savefig("boxploty\\"+str(who_II30.columns[i])+"_30.png")
    # boxplot135.figure.savefig("boxploty\\"+str(who_II135.columns[i])+"_135.png")

plt.show()
    