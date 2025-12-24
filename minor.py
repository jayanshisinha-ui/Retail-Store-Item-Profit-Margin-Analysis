import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail_profit_margin.csv")
print(df)

# formula for calculating the profit margin 
df["Profit_Margin"] = ((df["Selling_Price"] - df["Cost_Price"])  / df["Cost_Price"]) * 100
print(df[["Item_Name", "Profit_Margin"]])

# Product Category comparison 
category_groups = df.groupby("Category")
print(category_groups.size())

# Calculating mean 
mean_profit = category_groups["Profit_Margin"].mean()
print("Mean Profit Margin by Category:\n", mean_profit)

# Calculating standrad deviation
std_profit = category_groups["Profit_Margin"].std()
print("Standard Deviation by Category:\n", std_profit)

#Combined Mean & Standard Deviation Table
stats_table = pd.DataFrame()
stats_table['Mean']=mean_profit
stats_table['Standard Deviation']=std_profit
print(stats_table)

#Box Plot for Profit Margin
plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Profit_Margin', data=df)
plt.title('Retail Store Item Profit Margin Analysis by Category')
plt.xlabel('Product Category')
plt.ylabel('Profit Margin (%)')
plt.show()
