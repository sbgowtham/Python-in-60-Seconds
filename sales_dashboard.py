import streamlit as st
import pandas as pd

# 1. Create Sample Data Directly
data = {
"Month":["Jan","Feb","Mar","Apr","May"],
"Sales":[1000, 1200, 900, 1300, 1500],
"Expenses":[700, 600, 750, 2000, 900]
}
df = pd.DataFrame(data)

# 2. Build a Simple Dashboard
st.title("My Quick Dashboard")
st.write("Data Preview", df.head())

# 3. Display a Simple Line Chart
st.line_chart(df[["Sales", "Expenses"]])
