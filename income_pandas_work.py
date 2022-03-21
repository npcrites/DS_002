traits = ['workclass', 'fnlwgt', 'education', 'educational-num', 'marital-status','occupation', 'relationship','race','gender','capital-gain','capital-loss','hours-per-week', 'native-country','income']

import numpy as np
import pandas as pd
import sklearn as sk

# Plotting cell
import seaborn as sns
from matplotlib import pyplot as plt

# font
plt.rcParams.update({'font.size': 8})

# reset the default figsize value
plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]

# 144 is good for a high-resolution display. Try 100 if it's too big
plt.rcParams["figure.dpi"] = (120)

ac=pd.read_csv('adult_cleaned.csv')
ac

ac.info

ac.isnull().sum()

ac.dropna(how='any', inplace=True)
ac.isnull().sum()

print(f"We have {ac.duplicated().sum()} duplicate values")

ac = ac.drop_duplicates()

print(f"After dropping duplicate values, now we have {ac.duplicated().sum()} duplicate values")

ac = ac.drop(['capital-gain', 'capital-loss'], axis=1)

myDict = {'Federal-gov':1, 'Local-gov':2, 'Private':3,'Self-emp-inc':4,'Self-emp-not-inc':5,'State-gov':6,'Without-pay':7,}

categorical_workclass = []
for i, workclass in enumerate(ac['workclass']):
    if workclass == '?':
        categorical_workclass.append(8)
    else:
        categorical_workclass.append(myDict[workclass])
ac["categorical_workclass"] = categorical_workclass

#drops
ac = ac.drop(['workclass'], axis = 1)
ac = ac.drop(['education'], axis = 1)

Ismarried = {'Married-civ-spouse':1, 'Never-married':2, 'Divorced':3, 'Widowed':4,
       'Separated':5, 'Married-spouse-absent':6, 'Married-AF-spouse':7}

num_marital_status = []
for i, married in enumerate(ac['marital-status']):
    if pd.isnull(married):
        num_marital_status.append(8)
    else:
        num_marital_status.append(Ismarried[married])
ac["num_maritial_status"] = num_marital_status

#drop
ac = ac.drop(['marital-status'], axis = 1)

occup_dict = {'Craft-repair':1, 'Handlers-cleaners':2, '4-service':3, 'Adm-clerical':4,
       'Farming-fishing':5, 'Sales':6, 'Prof-specialty':7, 'Priv-house-serv':8,
       'Transport-moving':9, 'Exec-managerial':10, 'Machine-op-inspct':11,
       'Protective-serv':12, 'Tech-support':13, 'Armed-Forces':14}

occup_num = []
for i, occupation in enumerate(ac['occupation']):
    if pd.isnull(occupation):
        occup_num.append(15)
    elif occupation == '?':
        occup_num.append(16)
    else:
        occup_num.append(occup_dict[occupation])
ac["occupation-num"] = occup_num

#drop
ac = ac.drop(['occupation'], axis = 1)

relations_dict = {'Husband':1, 'Own-child':2, 'Not-in-family':3, 'Unmarried':4, '4-relative':5,
       'Wife':6}

rel_num = []
for i, rel in enumerate(ac['relationship']):
    if pd.isnull(rel):
        rel_num.append(7)
    elif occupation == '?':
        rel_num.append(8)
    else:
        rel_num.append(relations_dict[rel])
ac["relationship-num"] = rel_num

#drop
ac = ac.drop(['relationship'], axis = 1)

ac['native-country'].unique()

native_dict = {}

for i, country in enumerate(ac['native-country'].unique()):
    native_dict[country] = i+1

native_country_num = []
for i, country in enumerate(ac['native-country']):
    native_country_num.append(native_dict[country])
ac["native-country-num"] = native_country_num

#drop
ac = ac.drop(['native-country'], axis = 1)

# Load it into a Pandas Dataframe
# zoo=Zoo.iloc[:,1:]

# Get a list of the animal classes to test the predictions (the TARGET)
y=ac['income'].values

# Remove the `type` and `animal name` from the **training data** (this is the DATA)
X=ac.drop(['age','income'],axis=1).values

# Haave a look. Do you need to normalize the data? Look at the numeric columns:
ac.describe()

# Split the data into train and test sets
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# See how `y=zoo['type'].values` encodes the TARGET types into integers:

y = y.reshape(-1,1)


# How many animals in each target type? 
type_names = ["less than 50k/yr", "more than 50k/yr"]

from collections import Counter
c = Counter(ac.income)
print(c)

ct = {}
for i,t in enumerate(type_names):
  print(type_names[i],c[i])
  ct[type_names[i]] = c[i]
    #CHECK THIS

ct

# What is the best value for k?'
# Try the elbow method

from sklearn.neighbors import KNeighborsClassifier

numpts = int(len(ac)/6) # about 15% of the number of rows in the data
error_rate = []
error_rate1 = []

# This might take some time!
for i in range(1,20):
  knn = KNeighborsClassifier(n_neighbors=i)
  knn.fit(X_train,y_train)
  pred_i = knn.predict(X_test)
  error_rate.append(np.mean(pred_i != y_test))
  pred_j = knn.predict(X_train)
  error_rate1.append(np.mean(pred_j != y_train))

plt.figure(figsize=(10,6))
plt.plot(range(1,20),error_rate,color='blue', 
         linestyle='dashed', marker='o',markerfacecolor='red', markersize=7)
plt.plot(range(1,20),error_rate1,color='gray', 
         linestyle='dashed', marker='^',markerfacecolor='green', markersize=7)

plt.legend(['testing data','training data'])
plt.title('Error Rate vs. value of k')
plt.xlabel('k value')
plt.ylabel('Error Rate')


plt.show()

k=11
knn = KNeighborsClassifier(n_neighbors=11)
knn.fit(X_train,y_train)

knn.score(X_train,y_train), knn.score(X_test,y_test)

# Plot non-normalized confusion matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

titles_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        knn,
        X_test,
        y_test,
        display_labels=type_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)

    print(title)
    # print(disp.confusion_matrix)

plt.show()

y_pred = []
for i in X_test:
    y_pred.append(knn.predict(i.reshape(1,-1)))
from sklearn.metrics import classification_report
classification_report(y_test, y_pred, zero_division=0)

# We set the type_names at the top
print(classification_report(y_test, y_pred, target_names=type_names))
    

