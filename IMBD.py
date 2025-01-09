import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as nm

# Read the CSV file
file_path = "C:/Users/deepa/Downloads/imdb_movies.csv"
df= pd.read_csv(file_path)

# Ensure the column 'date_x' exists before converting
if "date_x" in df.columns:
    # Convert the 'date_x' column to datetime format
      df["date_x"] = pd.to_datetime(df["date_x"])
    # Print the 'date_x' column
      print(df["date_x"])
else:
    print("Column date_x doesnot exist in the csv file")

# Calculate and print the sum of null values in each column
null_counts = df.isnull().sum()
print(null_counts)

#filling the null values
if "genre" in df.columns:
    df["genre"]= df["genre"].fillna("Unavailable")
    print(df["genre"])
else:
    print("column genre does not exist in the csv file")

if "crew" in df.columns:
    df["crew"]= df["crew"].fillna("Unavailable")
    print(df["crew"])
else:
    print("column crew does not exist in the csv file")

sns.histplot(x="score", data=df, bins=20)
plt.show()

group_by= df.groupby("genre").agg({"names":"count"})
print(group_by.head(10))

plt.figure(figsize= (12, 4))
sns.barplot(x=group_by.index, y= group_by["names"], data=group_by) 
plt.xticks(rotation= 45)
plt.show()

sns.scatterplot(x="budget_x", y="revenue", data=df)
plt.show()

plt.figure(figsize=(12,4))
sns.boxplot(x= "country", y="score", data=df)
plt.xticks(rotation=45)
plt.show()

# Select the specified columns 
df1 = df[["score", "budget_x", "revenue"]] 

# Calculate the correlation matrix 
correlation_matrix = df1.corr() 

# Print the correlation matrix 
print(correlation_matrix)

sns.heatmap(correlation_matrix,annot=True)
plt.show()

gb= df.groupby("genre").agg({"score":"mean"})
gb= gb.sort_values(by="score", ascending=False)
gb= gb.head(20)

plt.figure(figsize=(12,4))
sns.barplot(x=gb.index, y=gb["score"], data=gb, hue=gb.index, palette="viridis")
plt.xticks(rotation=90)
plt.show()

df["year"]= df["date_x"].dt.strftime("%Y")
plt.figure(figsize=(12,4))
sns.countplot(x="year", data=df)
plt.xticks(rotation=90,fontsize = 8)
plt.show()
