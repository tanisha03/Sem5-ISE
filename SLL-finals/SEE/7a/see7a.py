import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

data = pd.read_csv("iris.csv")
print("=================================DATA HEADERS================================")
print(data.head())

print("===============================DATA DESCRIPTION==============================")
print(data.info())
print(data.describe())

print("=====================================THIRD====================================")
data1 = data.drop(["petal.length"],axis =1)
print(data1.head())

print("=====================================FOURTH====================================")
print(data[["variety","petal.width"]].groupby(["variety"],as_index = True).mean())

print("=====================================FIFTH====================================")
ax = sns.countplot(x="sepal.width", hue="variety",palette ="Set1",data = data)
ax.set(title="CATEGORIZATION OF FLOWERS BASED ON SEPAL WIDTH",xlabel = "CATEGORIES",ylabel= "TOTAL")
plt.show()
