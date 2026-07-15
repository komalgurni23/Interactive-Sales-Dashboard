# ==========================================
# Interactive Sales Dashboard
# ==========================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -----------------------------
# Create visualization folder
# -----------------------------
os.makedirs("visualizations", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

print("="*60)
print("DATASET PREVIEW")
print("="*60)
print(df.head())

print("\nDataset Shape :", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# Data Cleaning
# -----------------------------
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# -----------------------------
# Seaborn Theme
# -----------------------------
sns.set(style="whitegrid")

# ==========================================
# 1. Line Chart
# ==========================================

plt.figure(figsize=(10,5))

sns.lineplot(
    data=df,
    x="Date",
    y="Total_Sales",
    marker="o"
)

plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/line_chart.png")
plt.show()

# ==========================================
# 2. Bar Chart
# ==========================================

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x="Product",
    y="Total_Sales"
)

plt.title("Sales by Product")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/bar_chart.png")
plt.show()

# ==========================================
# 3. Scatter Plot
# ==========================================

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Price",
    y="Total_Sales",
    hue="Region",
    s=100
)

plt.title("Price vs Total Sales")

plt.tight_layout()
plt.savefig("visualizations/scatter_plot.png")
plt.show()

# ==========================================
# 4. Box Plot
# ==========================================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="Product",
    y="Price"
)

plt.title("Price Distribution by Product")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/box_plot.png")
plt.show()

# ==========================================
# 5. Heatmap
# ==========================================

plt.figure(figsize=(8,6))

corr = df[["Quantity","Price","Total_Sales"]].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("visualizations/heatmap.png")
plt.show()

# ==========================================
# Plotly Interactive Bar Chart
# ==========================================

fig1 = px.bar(
    df,
    x="Product",
    y="Total_Sales",
    color="Region",
    title="Interactive Sales by Product"
)

fig1.show()

# ==========================================
# Plotly Line Chart
# ==========================================

fig2 = px.line(
    df,
    x="Date",
    y="Total_Sales",
    markers=True,
    title="Interactive Sales Trend"
)

fig2.show()

# ==========================================
# Plotly Pie Chart
# ==========================================

product_sales = df.groupby("Product", as_index=False)["Total_Sales"].sum()

fig3 = px.pie(
    product_sales,
    names="Product",
    values="Total_Sales",
    title="Sales Share by Product"
)

fig3.show()

# ==========================================
# Business Insights
# ==========================================

print("\n" + "="*60)
print("BUSINESS INSIGHTS")
print("="*60)

print("Total Revenue :", df["Total_Sales"].sum())

print("Average Revenue :", round(df["Total_Sales"].mean(),2))

print("Highest Revenue :", df["Total_Sales"].max())

print("Lowest Revenue :", df["Total_Sales"].min())

print("\nRevenue by Product")

print(df.groupby("Product")["Total_Sales"].sum())

print("\nRevenue by Region")

print(df.groupby("Region")["Total_Sales"].sum())

print("\nAverage Price :", round(df["Price"].mean(),2))

print("Average Quantity :", round(df["Quantity"].mean(),2))

print("\nDashboard Created Successfully")