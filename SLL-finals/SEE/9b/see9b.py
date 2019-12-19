import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

data = pd.read_csv("blackfriday.csv")

print("============================DATA HEADERS=============================")
print(data.head())

print("============================DATA DESCRIPTION=========================")
print(data.info())
print(data.describe())

print("============================THIRD====================================")
data["City_Category"] = data["City_Category"].fillna("B")
print(data["City_Category"] )

print("============================FOURTH===================================")
data["City_Category"] = data["City_Category"].map(
	{"A": "Metro Cities","B":"Small Towns","C": "Villages"})
print(data.head())

print("============================FIFTH===================================")
ax = sns.countplot(x="City_Category",hue ="Gender",palette = "Set1", data = data )
ax.set(title="CITY CATEGORY",xlabel="Categories",ylabel="Total")
plt.show()