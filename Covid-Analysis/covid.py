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

# Plot new deaths
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["new_deaths"])
plt.title("COVID-19 New Deaths Trend")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.show()
