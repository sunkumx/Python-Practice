# Write a Function to Filter Rows in a DataFrame Based on Conditions

#importing library
import pandas as pd

#sample data
data = {
    "sales":[500,1200,1500,2500],
    "region":["West", "East", "North", "South"]
}

df = pd.DataFrame(data)

avg_sales = df.groupby("region")["sales"].mean().reset_index()