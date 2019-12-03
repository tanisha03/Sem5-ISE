import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris_df = pd.read_csv("iris.csv")
print("---DataFrame---")
print(iris_df)
print("---info---")
print(iris_df.info())
print("---head---")
print(iris_df.head())

print("---Functions---")
print(iris_df[["variety", "petal.width"]].groupby(["variety"], as_index=True).mean())

ax = sns.countplot(x="sepal.width", hue="variety", data=iris_df, palette="Set1")
ax.set(
    title="Categorization of flowers based on sepal width",
    xlabel="Categories",
    ylabel="Total",
)
plt.show()

interval = (0, 1, 2, 3)
categories = ["<0", "1-2", ">2"]
iris_df["flowers_cats"] = pd.cut(iris_df["petal.width"], interval, labels=categories)
ax = sns.countplot(x="flowers_cats", data=iris_df, hue="variety", palette="Set2")
ax.set(
    xlabel="Flowers Categorical",
    ylabel="Total",
    title="Writing Marks Categorical Distribution",
)
plt.show()
