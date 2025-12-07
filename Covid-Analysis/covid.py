import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("covid.csv")

# Convert date column to datetime
data["date"] = pd.to_datetime(data["date"])

# Select important columns
df = data[["date", "new_cases", "new_deaths"]].fillna(0)

# Plot new cases
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["new_cases"])
plt.title("COVID-19 New Cases Trend")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("covid.csv")

# Show first few rows
print("Dataset Preview:")
print(df.head())

# Select required columns if available
columns_needed = ["location", "date", "total_cases", "total_deaths", "new_cases", "new_deaths"]

df = df[columns_needed]

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Drop missing values
df = df.dropna()

# --------------------------------------------------------------------
# 1. Top 10 Countries by Total Cases
# --------------------------------------------------------------------
latest = df[df["date"] == df["date"].max()]
top10 = latest.sort_values(by="total_cases", ascending=False).head(10)

print("\nTop 10 countries by total COVID cases:")
print(top10[["location", "total_cases"]])

top10.plot(x="location", y="total_cases", kind="bar", figsize=(10,5))
plt.title("Top 10 Countries by Total COVID Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 2. Death Rate Analysis
# --------------------------------------------------------------------
latest["death_rate"] = (latest["total_deaths"] / latest["total_cases"]) * 100

print("\nDeath Rates of Top 10 Countries:")
print(latest.sort_values(by="death_rate", ascending=False).head(10)[["location","death_rate"]])

# --------------------------------------------------------------------
# 3. Trend Line for India (example)
# --------------------------------------------------------------------
india = df[df["location"] == "India"]

india.plot(x="date", y="total_cases", figsize=(10,5))
plt.title("COVID-19 Case Trend in India")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.tight_layout()
plt.show()

print("\nAnalysis Complete!")

# Plot new deaths
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["new_deaths"])
plt.title("COVID-19 New Deaths Trend")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.show()
