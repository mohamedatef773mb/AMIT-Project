import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# load data
data=pd.read_csv("data/insurance.csv")

# Streamlit app
st.title("Insurance Data Dashboard")


# Data Preview
st.header("Data Overview")
st.write("First  few rows of the data:")
st.dataframe(data.head())

# Data Summary
st.header("Summary Statistics for numerical  columns")
st.dataframe(data.describe())

st.header("Summary Statistics for categorical  columns")
st.dataframe(data.describe(include=["object"]))


# Select Columns for Visualization

st.header("Data Visualization")
st.write("Select columns to visualize:")
X_axis=st.selectbox("X-axis",data.columns)
y_axis=st.selectbox("Y-axis",data.columns)

plot_type=st.radio("Select Plot Type:",["Scatter plot","Line plot","Histogram plot"],index=None)
# Plotting 
if plot_type=="Scatter plot":
    st.subheader("Scatter Plot")
    fig=plt.figure()
    sns.scatterplot(x=X_axis,y=y_axis,data=data)
    plt.xlabel(X_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type=="Line plot":
    st.subheader("Line Plot")
    fig=plt.figure()
    sns.lineplot(x=X_axis,y=y_axis,data=data)
    plt.xlabel(X_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type=="Histogram plot":
    st.subheader("Histogram Plot")
    fig=plt.figure()
    sns.histplot(x=X_axis,data=data)
    plt.xlabel(X_axis)
    st.pyplot(fig)
# Correlation Heatmap
st.header("Correlation Heatmap")
if st.button("Generate Heatmap"):
    fig=plt.figure()
    sns.heatmap(data.corr(numeric_only=True),annot=True,cmap="Blues")
    st.pyplot(fig)
st.write("Explore and Analyze your data")