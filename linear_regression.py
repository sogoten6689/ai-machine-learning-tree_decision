import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read data
df = pd.read_csv("./data.csv")
df.columns = ["index", "height", "weight"]
print("start")
print(df.head())

# plot data
# sns.pairplot(df, x_vars=["height", "weight"], y_vars=["height", "weight"], height=4, aspect=1, kind='reg')
# plt.show()
sns.scatterplot(data=df, x="height", y="weight")
# sns.pairplot(df, x_vars=["height", "weight"])
plt.show()

x = df["height"].values
y = df["weight"].values

# find m and b
N = x.shape[0]
# m = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / (N * np.sum(x * x) - np.sum(x) * np.sum(x))
# b = np.mean(y) - m * np.mean(x)

m = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / (N * np.sum(x ** 2) - (np.sum(x) ** 2))
b = (np.sum(y) - m * np.sum(x)) / N

print("m: ", m)
print("b: ", b)

print("end")