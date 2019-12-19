import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("student.csv")

print("=================================DATA HEADERS================================")
print(data.head())

print("===============================DATA DESCRIPTION==============================")
print(data.info())
print(data.describe())

print("=====================================THIRD====================================")
data1 = data.drop(["lunch", "test preparation course"], axis=1)
print(data1.head())

print("=====================================FOURTH====================================")
data["parental level of education"] = data["parental level of education"].fillna("high school")
print(data1["parental level of education"])

print("=====================================FIFTH====================================")
ax = sns.countplot(x="test preparation course", hue="gender", palette="Set1", data=data)
ax.set(title="Test Preparation", xlabel="Course", ylabel="Total")
plt.show()




