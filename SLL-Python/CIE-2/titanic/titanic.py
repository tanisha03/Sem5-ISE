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

titanic_df = titanic_df.drop(["Name", "PassengerId", "Ticket"], axis=1)
titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")

titanic_df.groupby(["Sex"], as_index=False).mean()

titanic_df[["Sex", "Survived"]].groupby(["Sex"], as_index=False).mean().sort_values(
    by="Survived", ascending=False
)


def get_person(passenger):
    age, sex = passenger
    return "child" if age < 16 else sex


titanic_df["Person"] = titanic_df[["Age", "Sex"]].apply(get_person, axis=1)

# person_dummies_titanic = pd.get_dummies(titanic_df["Person"])
# person_dummies_titanic.columns = ["Child", "Female", "Male"]
# person_dummies_titanic.drop(["Male"], axis=1, inplace=True)


titanic_df["Survived"] = titanic_df["Survived"].map({0: "Died", 1: "Survived"})
print(titanic_df.Survived)
ax = sns.countplot(x="Pclass", hue="Survived", palette="Set1", data=titanic_df)
ax.set(
    title="Passenger status (Survived/Died) against Passenger Class",
    xlabel="Passenger Class",
    ylabel="Total",
)
plt.show()

ax = sns.countplot(x="Sex", hue="Survived", palette="Set2", data=titanic_df)
ax.set(title="Total Survivors According to Sex", xlabel="Sex", ylabel="Total")
plt.show()

interval = (0, 18, 35, 60, 120)
categories = ["Children", "Teens", "Adult", "Old"]
titanic_df["Age_cats"] = pd.cut(titanic_df.Age, interval, labels=categories)
ax = sns.countplot(x="Age_cats", data=titanic_df, hue="Survived", palette="Set3")
ax.set(
    xlabel="Age Categorical",
    ylabel="Total",
    title="Age Categorical Survival Distribution",
)
plt.show()

