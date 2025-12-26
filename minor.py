import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail_profit_margin.csv")
print(df)

# Calculating the profit margin 
df["Profit Margin"] = ((df["Selling_Price"] - df["Cost_Price"])  / df["Cost_Price"]) * 100
print(df[["Item_Name", "Profit Margin"]])

# Product Category comparison 
category_grp = df.groupby("Category")
print(category_grp.size())

# Calculating mean 
mean = category_grp["Profit Margin"].mean()
print("Mean Profit Margin by Category:\n", mean)

# Calculating standrad deviation
std = category_grp["Profit Margin"].std()
print("Standard Deviation by Category:\n", std)

#Combined Mean & Standard Deviation Table
s_table = pd.DataFrame()
s_table['Mean']=mean
s_table['Standard Deviation']=std
print(s_table)

#Box Plot for Profit Margin
plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Profit Margin', data=df)
plt.title('Retail Store Item Profit Margin Analysis by Category')
plt.xlabel('Product Category')
plt.ylabel('Profit Margin (%)')
plt.show()
