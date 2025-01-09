#steps of building a machine learning model:
#1. Gaining the understanding of the project and  what it is about
#2. Import libraries (atleat initial ones like pandas,numpy,seaborn, matpltlib.pyplot)
#3. Import the data/ get the data
#4. Data cleaning and understanding
#5. EDA: Exploratory data analysis
#  5.1 Univariate analysis- to look at the distribution in order to understand if there is any outlier present
#  5.2 Bi-variant analysis- when we look at the relationship between 2 variables (target variable= the variable we have to perdict)
#  5.3 Multi-variant analysis- to check correlationbetween all the combination of features


#data has 2 type: 1. numerical data 2. categorical data
#Exploratory Data Analysis (EDA): EDA to understand the relationships between different features and the target variable (price).
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LinearRegression

file_path= "c:/Users/deepa/Downloads/Cardekho.csv"
df= pd.read_csv(file_path)

#Basic data check
df.info()

df.shape

summary_data= df.describe()
print(summary_data)

brand_occurance= df['brand'].value_counts()
print(brand_occurance)

car_occurance= df['car_name'].value_counts(normalize=True)*100 #normalize gives how much it contribute to the data
print(car_occurance)

#visual representation
mileage_mean= df['mileage'].mean()
print(mileage_mean)

mileage_ploting=sns.kdeplot(x= df['mileage'], color='r')
plt.show()

engine_ploting= sns.kdeplot(x=df['engine'], color='g')
plt.show()

seats_ploting= sns.kdeplot(x=df['seats'], color='b')
plt.show()

vehicle_age_ploting= sns.kdeplot(df['vehicle_age'], color='y')
plt.show()

km_driven_ploting= sns.kdeplot(df['km_driven'], color='r')
plt.show()

max_power_ploting= sns.kdeplot(df['max_power(BHP)'], color='y')
plt.show()
values=df[df['max_power(BHP)']>400]
print(values)

selling_price_ploting= sns.kdeplot(df['selling_price'], color='b')
plt.show()

seller_type_ploting= sns.countplot(x=df['seller_type'])
plt.show()

plt.figure(figsize= (12, 4))
car_name_ploting= sns.countplot(x=df['car_name'])
plt.xticks(rotation= 90)
plt.show()

plt.figure(figsize=(12,4))
brand_ploting= sns.countplot(x=df['brand'])
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12,4))
fuel_type_ploting= sns.countplot(x=df['fuel_type'])
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12,4))
transmission_type_ploting= sns.countplot(x=df['transmission_type'])
plt.xticks(rotation=90)
plt.show()

# Bi-variant anlysis: lets look at the relationship of different variables with the selling price(target variable)
sns.scatterplot(data= df, x='selling_price', y='vehicle_age', color='g')
plt.show()

sns.scatterplot(data=df, x='selling_price', y='mileage', color='r')
plt.show()

sns.scatterplot(data=df, x='selling_price', y='engine', color='y')
plt.show()

sns.scatterplot(data=df, x='selling_price', y='max_power(BHP)', color='g')
plt.show()

sns.scatterplot(data=df, x='selling_price', y='seats', color= 'r')
plt.show()
#vehicle age, km driven, max power are impacting the price

#Multi-variant analysis(numerical features only)
features= ['vehicle_age', 'km_driven', 'mileage', 'max_power(BHP)', 'seats', 'selling_price']
print(features)

correlation_matrix=df[features].corr()
print(correlation_matrix)

sns.heatmap(data=df[features].corr(), annot=True)
plt.show()

# Create a copy of the DataFrame
model_data = df.copy()

model_data.drop(labels=['car_name', 'brand','model','seller_type'],axis=1, inplace=True)
print(model_data)

model_data= pd.get_dummies(model_data,dtype=int)
print(model_data)
 
# Linear regression- modelling: 
# Y(target variable i.e selling price)= m1x1 + m2x2 + m3x3.... x1,x2 are variables like vehicel age etc

x= model_data.drop('selling_price', axis=1) #independent variables
print(x)

#for getting the target variable we will just have selling_price
y= model_data['selling_price']
print(y)

# divide the data to train and test
train_x, test_x, train_y, test_y= train_test_split(x,y, test_size=0.2)
print(train_x) 

#applying regression to train the model:
regressor= LinearRegression().fit(train_x, train_y)
print(regressor)

# getting the prediction 
prediction= regressor.predict(test_x)
print(prediction)

test_x['predicted_sales_price']= prediction
test_x['actual_sales_price']= test_y
test_x["difference"]= test_x['predicted_sales_price']-test_x['actual_sales_price']
print(test_x)

