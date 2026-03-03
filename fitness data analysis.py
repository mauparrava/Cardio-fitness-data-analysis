import numpy as np
import pandas as pd
mydata = pd.read_csv(r'C:\python\PythonProject2\CardioGoodFitness.csv')
mydata.head()
mydata.describe(include="all")
mydata.info()
import matplotlib.pyplot as plt


mydata.hist(figsize=(20,30))
import seaborn as sns #importing seaborn library

sns.boxplot(x="Gender", y="Age", data=mydata)
sns.boxplot(x="Product", y="Age", data=mydata)
pd.crosstab(mydata['Product'],mydata['Gender'] )
pd.crosstab(mydata['Product'],mydata['MaritalStatus'] )
sns.countplot(x="Product", hue="Gender", data=mydata)
pd.pivot_table(mydata, index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'], aggfunc=len)

pd.pivot_table(mydata,'Income', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])
pd.pivot_table(mydata,'Miles', index=['Product', 'Gender'],
                     columns=[ 'MaritalStatus'])

sns.pairplot(mydata)
mydata['Age'].std()
mydata['Age'].mean()
sns.displot(data=mydata, x='Age', kde=True)
plt.show()
sns.pairplot(mydata)

mydata.hist(by='Gender',column = 'Age')

mydata.hist(by='Gender',column = 'Income')
mydata.hist(by='Gender',column = 'Miles')

mydata.hist(by='Product',column = 'Miles', figsize=(20,30))
corr = mydata.corr(numeric_only = True)
sns.heatmap(corr, annot=True)

#Load function from sklearn
from sklearn import linear_model

# Create linear regression object
regr = linear_model.LinearRegression()

y = mydata['Miles']
x = mydata[['Usage','Fitness']]

# Train the model using the training sets
regr.fit(x,y)

# MilesPredicted = -56.74 + 20.21*Usage + 27.20*Fitness