
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr

def analyze_profit_margin(file):
    df = pd.read_csv(file.name)

    # Calculating the profit margin 
    df["Profit Margin"] = ((df["Selling_Price"] - df["Cost_Price"]) / df["Cost_Price"]) * 100

    # Category Comparison
    category_grp = df.groupby("Category")
    mean = category_grp["Profit Margin"].mean()
    std = category_grp["Profit Margin"].std()

    # Combined table
    s_table = pd.DataFrame({
        "Mean Profit Margin": mean,
        "Standard Deviation": std
    })

    # Box Plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Category', y='Profit Margin', data=df)
    plt.title('Retail Store Profit Margin Analysis by Category')
    plt.xlabel('Product Category')
    plt.ylabel('Profit Margin (%)')
    plot_path = "boxplot.png"
    plt.savefig(plot_path)
    plt.close()

    return df, s_table, plot_path


# Gradio UI
ui =gr.Interface(
    fn=analyze_profit_margin,
    inputs=gr.File(label="Upload Retail Profit CSV"),
    outputs=[
        gr.DataFrame(label="Full Dataset with Profit Margin"),
        gr.DataFrame(label="Mean & Standard Deviation Table"),
        gr.Image(label="Profit Margin Boxplot")
    ],
    title="Retail Store Profit Margin Analyzer",
    description="Upload your retail dataset CSV to view category-wise profit margin analysis."
)

ui.launch()
