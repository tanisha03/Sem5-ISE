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

