import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv("Titanic.csv")

# preview the data
print("======Data Headers=======")
titanic_df.head()

print("=====Data Decription=====")
# column description
titanic_df.info()
titanic_df.describe()

titanic_df = titanic_df.drop(["Name"], axis=1)

titanic_df.groupby(["Sex"], as_index=False).mean()

titanic_df[["Sex", "Survived"]].groupby(["Sex"], as_index=False).mean().sort_values(
    by="Survived", ascending=False
)


def get_person(passenger):
    age, sex = passenger
    return "child" if age < 16 else sex


titanic_df["Person"] = titanic_df[["Age", "Sex"]].apply(get_person, axis=1)

# print(titanic_df["Person"])


person_dummies_titanic = pd.get_dummies(titanic_df["Person"])
person_dummies_titanic.columns = ["Child", "Female", "Male"]
person_dummies_titanic.drop(["Male"], axis=1, inplace=True)


# titanic_df = titanic_df.join(person_dummies_titanic)
# print(titanic_df)
# fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(10, 5))
# g = sns.factorplot("Pclass", data=titanic_df, kind="count", ax=axis1)

print(person_dummies_titanic)

person_perc = (
    titanic_df[["Person", "Survived"]].groupby(["Person"], as_index=False).mean()
)
print(person_perc)

sns.barplot(
    x="Person", y="Survived", data=person_perc, order=["male", "female", "child"],
)
plt.show()
"""No of passedngers in each group """


facet = sns.FacetGrid(titanic_df, hue="Survived", aspect=4)
facet.map(sns.kdeplot, "Age", shade=True)
facet.set(xlim=(0, titanic_df["Age"].max()))
facet.add_legend()
plt.show()
