#%%time
# Ignore warnings
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from matplotlib import style
from sklearn.model_selection import train_test_split
style.use('fivethirtyeight')
from sklearn.neighbors import KNeighborsClassifier

# Dane
# patients = pd.read_csv('good_allOK.csv',sep=',',names=['Gln_30','Ins_30', 'MM09_30', 'MM12_30','MM20_30', 'NAA_30','TNAA_30', 'TCho_30', 'TCr_30','Glx_30', 'TLM09_30', 'TLM13_30', 'TLM20_30','Glth_135',
#                                                  'TCho_135','Glx_135','GROUP'])

patients = pd.read_csv('ready_all.csv')

features = patients.iloc[:,:-1].copy()

group = patients['GROUP'].copy()

# zbiór testowy i uczący
features_train, features_test, y_train, y_test = train_test_split(features,group,test_size=0.2,random_state=0) 

# skalowanie cech - zerowa średnia i jednostkowy błąd standardowy
for col in features_train.columns:
    features_train[col] = StandardScaler().fit_transform(features_train[col].values.reshape(-1,1))

# wektory średnie
mean_all = np.mean(features_train,axis=0).values.reshape(13,1) # zero
mean_class = []
for i,uni in enumerate(np.unique(patients['GROUP'])):
    mean_class.append(np.mean(features_train.where(patients['GROUP']==uni),axis=0))
mean_class = np.array(mean_class).transpose()

# macierz rozproszenia
pats_SW = []
Nc = []
for i,uni in enumerate(np.unique(patients['GROUP'])):
    a = np.array(features_train.where(patients['GROUP']==uni).dropna().values-mean_class[:,i].reshape(1,13))
    pats_SW.append(np.dot(a.transpose(),a))
    Nc.append(np.sum(patients['GROUP']==uni))
SW = np.sum(pats_SW,axis=0)
SB = np.dot(Nc*np.array(mean_class-mean_all),np.array(mean_class-mean_all).T)
   
# wartości własne i wektory własnie
eigval, eigvec = np.linalg.eig(np.dot(np.linalg.inv(SW),SB))
    
# dwie największe wartości własne
eigen_pairs = [[np.abs(eigval[i]),eigvec[:,i]] for i in range(len(eigval))]
eigen_pairs = sorted(eigen_pairs,key=lambda k: k[0],reverse=True)
w = np.hstack((eigen_pairs[0][1][:,np.newaxis].real,eigen_pairs[1][1][:,np.newaxis].real))

# Y=features*w
Y = features_train.dot(w)

# wykresy
fig = plt.figure()
ax0 = fig.add_subplot(111)

for l,c,m in zip(np.unique(y_train),['r','g','b','c','m'],['s','x','o','^','d']):
    ax0.scatter(Y[0][y_train==l],
                Y[1][y_train==l],
               c=c, marker=m, label=l,edgecolors='black')
ax0.legend(loc='upper right')

# punkty średnie klas
means = []
for m,group in zip(['s','x','o','^','d'],np.unique(y_train)):
    means.append(np.mean(Y[y_train==group],axis=0))
    ax0.scatter(np.mean(Y[y_train==group],axis=0)[0],np.mean(Y[y_train==group],axis=0)[1],marker=m,c='black',s=100)
# Diagram Woronoja   
mesh_x, mesh_y = np.meshgrid(np.linspace(-2.5,2.5),np.linspace(-2.5,2.5)) 
mesh = []
for i in range(len(mesh_x)):
    for j in range(len(mesh_x[0])):
        date = [mesh_x[i][j],mesh_y[i][j]]
        mesh.append((mesh_x[i][j],mesh_y[i][j]))
        
NN = KNeighborsClassifier(n_neighbors=1)

NN.fit(means,['r','g','b','c','m'])        
predictions = NN.predict(np.array(mesh))
ax0.scatter(np.array(mesh)[:,0],np.array(mesh)[:,1],color=predictions,alpha=0.3)
plt.show()