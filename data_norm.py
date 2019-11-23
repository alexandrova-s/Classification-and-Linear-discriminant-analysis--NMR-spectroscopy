import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import io
import statistics as st
import math
import sklearn.preprocessing as pre

normed_results = pd.read_csv('results_all2.csv', index_col = "patients")


x = normed_results.values #returns a numpy array
min_max_scaler = pre.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
normed_results = pd.DataFrame(x_scaled)

normed_results.to_csv(r'normed_results.csv')