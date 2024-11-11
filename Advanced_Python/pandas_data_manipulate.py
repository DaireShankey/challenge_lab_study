# pandas_operations.py
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df)

# Filter rows based on condition
adults = df[df["Age"] > 26]
print("Adults:\n", adults)

# Add a new column
df["Occupation"] = ["Engineer", "Doctor", "Artist"]
print("Updated DataFrame:\n", df)

# Group by City and calculate mean age
grouped = df.groupby("City").mean()
print("Grouped by city:\n", grouped)
