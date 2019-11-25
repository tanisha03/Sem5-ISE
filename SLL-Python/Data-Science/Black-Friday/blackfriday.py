import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("BlackFriday.csv")

print("======Data Headers=======")
print(data.head())

print("=====Data Decription=====")
print(data.info())
print(data.describe())

data=data.drop(['User_ID', 'Product_ID', 'Stay_In_Current_City_Years'], axis=1)
print(data.head())

data["City_Category"] = data["City_Category"].fillna("B")
print(data["City_Category"])

data["City_Category"] = data['City_Category'].map({
    "A": "Metro Cities",
    "B": "Small Towns",
    "C": "Villages"
})


data["Marital_Status"] = data['Marital_Status'].map({
    1: "Married",
    0: "Un-married"
})

data.rename(columns={"Product_Category_1":"Baseball Caps","Product_Category_2":"Wine tumblers","Product_Category_3":"Pet Raincoats"},inplace=True)

data["Wine tumblers"] = data["Wine tumblers"].fillna("5")
data["Pet Raincoats"] = data["Pet Raincoats"].fillna("10")

print(data.head(10))

ax = sns.countplot(x="Baseball Caps", hue="Gender", palette="Set1", data=data)
ax.set(title="Product Category 1", xlabel="Categories", ylabel="Total")
plt.show()

ax = sns.countplot(x="Wine tumblers", hue="Gender", palette="Set1", data=data)
ax.set(title="Product Category 2", xlabel="Categories", ylabel="Total")
plt.show()

ax = sns.countplot(x="City_Category", hue="Gender", palette="Set1", data=data)
ax.set(title="City Category", xlabel="Categories", ylabel="Total")
plt.show()