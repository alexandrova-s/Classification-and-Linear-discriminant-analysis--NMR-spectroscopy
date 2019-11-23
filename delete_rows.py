import pandas as pd
import suspect
import numpy as np
from matplotlib import pyplot as plt
import os
#%matplotlib inline


directory = os.fsencode(".\Badania\second\\")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith("csv"):
        csv = pd.read_csv(".\Badania\second\\" + filename, header=1, index_col=0)
        df_csv = pd.DataFrame(data=csv)
        df_csv.index = pd.Series(df_csv.index).replace(np.nan, 'No label')
        df_csv.index = pd.Series(df_csv.index).replace('1-1-1', 'patient')
        df_csv = df_csv.drop(index='No label')
        df_csv = df_csv.drop(index='PPMScale')
        df_csv = df_csv.loc['patient', :]
        df_csv = df_csv.iloc[:, 1115:1612]
        df_csv.to_csv(".\Badania\second\\good\\" + filename)
