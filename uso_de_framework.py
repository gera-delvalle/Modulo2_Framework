# -*- coding: utf-8 -*-
"""Uso de Framework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ewD1mP3rxR1JGxVxxmSx7xJCLCB9XN5

# Bosque Aleatorio
"""

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

"""## Clasificacion"""

df = pd.read_csv('/content/drive/MyDrive/Inteligencia Artificial Avanzada/car_data.csv')

df.head()

from sklearn import preprocessing
gender = preprocessing.LabelEncoder()
gender.fit(df['Gender'].unique().tolist())
df['Gender'] = gender.transform(df['Gender'])

df

from sklearn.model_selection import train_test_split

X = df.drop(['Purchased','User ID'], axis = 1) 
y = df['Purchased']   

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

"""# Modelo simple"""

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier()

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

cf_matrix = confusion_matrix(y_test, y_pred)
ax = sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
            fmt='.2%', cmap='Blues')

ax.set_title('Matriz de Confusión\n\n');
ax.set_xlabel('\nValores Predecidos')
ax.set_ylabel('Valores Actuales ');


ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])


plt.show()

from sklearn.metrics import roc_curve, auc
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)
roc_auc

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier(max_depth=6,random_state=0)

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from numpy.random import seed
from numpy.random import randint
# seed random number generator
seed(1)
# generate some integers
registros = randint(0, len(X_test), 5)
print(registros)

X_test_1 = X_test.values
y_test_1 = y_test.values

for i in registros:
  print("Genero: ", X_test_1[i][0], "Edad: ", X_test_1[i][1], "Salario: ", X_test_1[i][2])
  print("Valor esperado: ", y_test_1[i])
  print("Valor obtenido: ",y_pred[i])
  print("\t")

from sklearn.metrics import roc_curve, auc
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)
roc_auc

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

cf_matrix = confusion_matrix(y_test, y_pred)
ax = sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
            fmt='.2%', cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');


ax.xaxis.set_ticklabels(['False','True'])
ax.yaxis.set_ticklabels(['False','True'])


plt.show()

from sklearn.metrics import roc_curve, auc
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(false_positive_rate, true_positive_rate)
print(roc_auc)

"""# Regresion"""

df_1 = pd.read_csv('/content/drive/MyDrive/Inteligencia Artificial Avanzada/insurance.csv')

df_1

sex = preprocessing.LabelEncoder()
sex.fit(df_1['sex'].unique().tolist())
df_1['sex'] = sex.transform(df_1['sex'])

smoker = preprocessing.LabelEncoder()
smoker.fit(df_1['smoker'].unique().tolist())
df_1['smoker'] = smoker.transform(df_1['smoker'])

region = preprocessing.LabelEncoder()
region.fit(df_1['region'].unique().tolist())
df_1['region'] = region.transform(df_1['region'])

df_1.head()

X = df_1.drop(['charges'], axis = 1) 
y = df_1['charges']   

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

from sklearn.ensemble import RandomForestRegressor

forest=RandomForestRegressor(n_estimators=20,
                             max_depth=10,
                             criterion='mse',
                            )


forest.fit(X_train,y_train)

y_prediction = forest.predict(X_test)

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

score=r2_score(y_test,y_prediction)
print('r2 score is ',score)
print('mean_sqrd_error is==',mean_squared_error(y_test,y_prediction))
print('root_mean_squared error of is==',np.sqrt(mean_squared_error(y_test,y_prediction)))

g=plt.plot(y_test - y_prediction,marker='o',linestyle='')

from sklearn.ensemble import RandomForestRegressor

forest=RandomForestRegressor(n_estimators= 100, min_samples_split= 10, min_samples_leaf= 4,  max_depth= 50, bootstrap= True)


forest.fit(X_train,y_train)

y_prediction = forest.predict(X_test)

seed(2)
# generate some integers
registros_2 = randint(0, len(X_test), 5)
print(registros_2)

X_test_1 = X_test.values
y_test_1 = y_test.values

X_test_1

for i in registros_2:
  print("Edad: ", X_test_1[i][0], "Sexo: ", X_test_1[i][1], "BMI: ", X_test_1[i][2], "Hijos: ", X_test_1[i][3], "Fumador: ", X_test_1[i][4], "Region: ", X_test_1[i][5])
  print("Valor esperado: ", y_test_1[i])
  print("Valor obtenido: ",y_prediction[i])
  print("\t")

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

score=r2_score(y_test,y_prediction)
print('r2 score is ',score)
print('mean_sqrd_error is==',mean_squared_error(y_test,y_prediction))
print('root_mean_squared error of is==',np.sqrt(mean_squared_error(y_test,y_prediction)))

g=plt.plot(y_test - y_prediction,marker='o',linestyle='')

