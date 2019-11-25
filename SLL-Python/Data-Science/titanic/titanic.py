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

titanic_df = titanic_df.drop(["PassengerId", "Name", "Ticket", "Parch"], axis=1)
