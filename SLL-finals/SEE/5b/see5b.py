import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("titanic.csv")
print("=================================DATA HEADERS================================")
print(data.head())

print("===============================DATA DESCRIPTION==============================")
print (data.info())
print (data.describe())

print("=====================================THIRD====================================")
data=data.drop(["Name"],axis=1)
print(data.head())

print("=====================================FOURTH====================================")
data["Sex"]=data["Sex"].fillna('Male')

data["Pclass"]=data["PClass"].fillna('2nd')

data["Survived"]=data["Survived"].fillna(0)

data["Survived"]=data["Survived"].map({
	0:"dead",
	1:"alive"})
print(data.head())

print("=====================================FIFTH====================================")
ax=sns.countplot(x="Survived", hue="PClass" ,palette="Set1", data=data)
ax.set(title="SURVIVED VS CLASS",xlabel="SURVIVAL",ylabel="TOTAL")
plt.show()