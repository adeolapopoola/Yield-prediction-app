import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import zipfile
import os


zip_file_path = 'Data/Dashboard_data (1).zip'
csv_file_name = 'Dashboard_data (1).xls'

# Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('Data')

# Read the CSV file
csv_file_path = os.path.join('Data', csv_file_name)
timeseries_df = pd.read_csv(r"C:\Users\deola\Downloads\Dashboard_data (1).xls", parse_dates=['Year'])
timeseries_df.set_index('Year', inplace=True)

def app():
    st.subheader('Dashboards')
    Country = st.selectbox('Select Country', timeseries_df['Country'].unique())
    Crop_type = st.selectbox('Select Crop Type', timeseries_df['Crop_type'].unique())

    filtered_df = timeseries_df[(timeseries_df['Country'] == Country) & (timeseries_df['Crop_type'] == Crop_type)]

    if not filtered_df.empty:
        # Time Series Plot
        fig = px.line(filtered_df, x=filtered_df.index, y='Yield(t/ha)', 
                      title=f'Time Series for {Crop_type} in {Country}', markers=True)
        fig.update_layout(xaxis_title='Year', yaxis_title='Yield(t/ha)')
                         #xaxis=dict(showgrid = False), yaxis= dict(showgrid = False))
        fig.update_layout(title_x=0.2)
        st.plotly_chart(fig)

        # Bar Chart: Annual Yield Comparison
        fig = px.bar(filtered_df, x=filtered_df.index.year, y='Yield(t/ha)', 
                     title=f'Annual Yield Comparison for {Crop_type} in {Country}', 
                     labels={'x': 'Year', 'Yield(t/ha)': 'Yield(t/ha)'})
        #fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.update_layout(title_x=0.15)
        st.plotly_chart(fig)

        # Scatter Plot: Yield vs Fertilizer Use
        fig = px.scatter(filtered_df, x='Nitrogen(t/ha)', y='Yield(t/ha)', 
                         title=f'Yield vs Fertilizer Use for {Crop_type} in {Country}', 
                         labels={'Nitrogen(t/ha)': 'Fertilizer Use Nitrogen(t/ha)', 'Yield(t/ha)': 'Yield(t/ha)'})
        #fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
        fig.update_layout(title_x=0.2)
        st.plotly_chart(fig)

        # Scatter Chart: Yield vs Average Annual Temperature
        fig = px.scatter(filtered_df, x='AverageTemperature', y='Yield(t/ha)', 
                         title=f'Yield vs Average Annual Temperature for {Crop_type} in {Country}', 
                         labels={'AverageTemperature': 'Average Temperature (°C)', 'Yield(t/ha)': 'Yield(t/ha)'})
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig)


        st.write(f"Time Series Data for {Crop_type} in {Country}:")
        st.dataframe(filtered_df)

    else:
        st.warning(f"No data available for the selected options")
