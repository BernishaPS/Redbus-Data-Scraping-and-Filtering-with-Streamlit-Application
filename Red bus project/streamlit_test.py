
import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\berni\Downloads\df_kerala_buses.csv")

# Title of the app
st.title("Kerala Buses Dataset")

# Display the raw dataset
st.header("Bus Data Overview")
st.write(df.head())

# Data filtering: User selection
st.sidebar.header("Filter options")

# Filter by Bus Type
bus_type = st.sidebar.multiselect(
    "Select Bus Type",
    options=df["Bus_type"].unique(),
    default=df["Bus_type"].unique()
)

# Filter by Source or Destination
source = st.sidebar.selectbox(
    "Select Source",
    options=df["Source"].unique()
)

destination = st.sidebar.selectbox(
    "Select Destination",
    options=df["Destination"].unique()
)

# Apply filters to the data
filtered_df = df[(df["Bus_type"].isin(bus_type)) & 
                 (df["Source"] == source) & 
                 (df["Destination"] == destination)]

# Display filtered data
st.header("Filtered Bus Data")
st.write(filtered_df)

# Additional Analysis - Display Basic Stats
st.header("Basic Statistics of the Filtered Data")
st.write(filtered_df.describe())


