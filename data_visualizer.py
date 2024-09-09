import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="Interactive Data Visualizer", page_icon=":bar_chart:", layout="wide")

st.markdown("""
    <style>
    .reportview-container {
        background: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background: #f5f5f5;
    }
    .css-1v0mbdj { 
        background: #009688;
        color: white;
    }
    .css-16fdm5m {
        font-family: 'Arial', sans-serif;
    }
    .css-1l02z6d {
        color: #009688;
        font-size: 1.5rem;
    }
    .stDownloadButton {
        background-color: #009688;
        color: white;
    }
    .stFileUploader {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Interactive Data Visualizer")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("## Data Preview")
    st.dataframe(df.head())
    
    st.write("## Basic Statistics")
    st.write(df.describe())

    st.write("## Visualization")
    chart_type = st.selectbox("Select Chart Type", ["Line", "Bar", "Scatter", "Pie"])
    
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    non_numeric_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()

    if chart_type in ["Line", "Bar", "Scatter"]:
        x_axis = st.selectbox("Select X-axis", options=numeric_columns)
        y_axis = st.selectbox("Select Y-axis", options=numeric_columns)

        if chart_type == "Line":
            plt.figure(figsize=(12,6))
            plt.plot(df[x_axis], df[y_axis], color='blue', marker='o')
            plt.title(f"{y_axis} vs {x_axis} (Line Chart)", fontsize=16)
            plt.xlabel(x_axis, fontsize=14)
            plt.ylabel(y_axis, fontsize=14)
            plt.grid(True)
            st.pyplot(plt)
        
        elif chart_type == "Bar":
            plt.figure(figsize=(12,6))
            plt.bar(df[x_axis], df[y_axis], color='green')
            plt.title(f"{y_axis} vs {x_axis} (Bar Chart)", fontsize=16)
            plt.xlabel(x_axis, fontsize=14)
            plt.ylabel(y_axis, fontsize=14)
            plt.grid(axis='y')
            st.pyplot(plt)
        
        elif chart_type == "Scatter":
            plt.figure(figsize=(12,6))
            sns.scatterplot(x=df[x_axis], y=df[y_axis], color='purple')
            plt.title(f"{y_axis} vs {x_axis} (Scatter Plot)", fontsize=16)
            plt.xlabel(x_axis, fontsize=14)
            plt.ylabel(y_axis, fontsize=14)
            plt.grid(True)
            st.pyplot(plt)

    elif chart_type == "Pie":
        if non_numeric_columns:
            column = st.selectbox("Select column for Pie Chart", options=non_numeric_columns)
            pie_data = df[column].value_counts()
            plt.figure(figsize=(8,8))
            plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
            plt.title(f"Distribution of {column}", fontsize=16)
            st.pyplot(plt)
        else:
            st.write("No categorical columns available for Pie Chart.")

    st.write("## Data Filtering")
    filter_column = st.selectbox("Select a column to filter", options=numeric_columns)
    min_value = st.number_input(f"Min value of {filter_column}", value=float(df[filter_column].min()))
    max_value = st.number_input(f"Max value of {filter_column}", value=float(df[filter_column].max()))

    filtered_data = df[(df[filter_column] >= min_value) & (df[filter_column] <= max_value)]
    st.write(f"Filtered Data based on {filter_column}:")
    st.dataframe(filtered_data)

    st.write("## Download Filtered Data")
    csv = filtered_data.to_csv(index=False)
    st.download_button("Download CSV", csv, "filtered_data.csv", "text/csv", key='download-csv')

else:
    st.write("Upload a CSV file to get started.")
