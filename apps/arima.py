import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import plotly.express as px
import plotly.graph_objects as go

#timeseries_df = pd.read_csv(r"C:\Users\deola\Downloads\Dashboard_data (1).xls", parse_dates=['Year'])
timeseries_df = pd.read_csv('Dashboard_data (1).xls', parse_dates=['Year'])
timeseries_df.set_index('Year', inplace=True)

def predict_arima(Year, Country, Crop_type, forecast_years):
    filtered_df2 = timeseries_df[
        (timeseries_df['Country'] == Country) & (timeseries_df['Crop_type'] == Crop_type)]
    arima = ARIMA(filtered_df2['Yield(t/ha)'], order=(5, 1, 1))
    arima_fit = arima.fit()
    
    start = len((filtered_df2))
    end = start + forecast_years-1 
    prediction = arima_fit.predict(start=start, end=end)
    last_date = filtered_df2.index[-1]
    predicted_series = pd.Series(list(prediction), 
                                 index=pd.date_range(start=last_date + pd.DateOffset(years=0), 
                                                     periods=len(prediction), freq='Y'))
    #predicted_series = pd.Series(list(prediction),
                                 #index=pd.date_range(start=filtered_df2.index[-1], periods=len(prediction), freq='Y'))

    return predicted_series


def app():
    st.subheader('Predictions with ARIMA Model')
    Country = st.selectbox('Select Country', timeseries_df['Country'].unique())
    available_crops = timeseries_df[timeseries_df['Country'] == Country]['Crop_type'].unique()
    Crop_type = st.selectbox('Select Crop Type', available_crops)
    #Crop_type = st.selectbox('Select Crop Type', timeseries_df['Crop_type'].unique())
    forecast_years = st.slider('Select Years Ahead for Forecast', 1, 10, 1)

    if st.button('Predict'):
        Year = timeseries_df.index.year.max()
        forecast = predict_arima(Year, Country, Crop_type, forecast_years)
        filtered_df2 = timeseries_df[
        (timeseries_df['Country'] == Country) & (timeseries_df['Crop_type'] == Crop_type)]
        
        st.write(f"ARIMA Forecast for {Crop_type} in {Country} for the next {forecast_years} years:")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=filtered_df2.index, y=filtered_df2['Yield(t/ha)'],
                                     mode='lines+markers', name='Observed', line = dict(color = '#00695c')))
        fig.add_trace(go.Scatter(x=forecast.index, y=forecast,
                                     mode='lines+markers', name='Forecast', line=dict(color='red')))
        fig.update_layout(title=f'ARIMA Forecast for {Crop_type} in {Country}',
                              xaxis_title='Year', yaxis_title='Yield(t/ha)', title_x=0.2)
                              #xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))
        st.plotly_chart(fig)


        #plt.figure(figsize=(10, 6))
        #plt.plot(filtered_df2.index, filtered_df2['Yield(t/ha)'], marker='o', linestyle='-', label='Observed')
        #plt.plot(forecast.index, forecast, marker='o', linestyle='-', color='r', label='Forecast')
        #plt.title(f'ARIMA Forecast for {Crop_type} in {Country}')
        #plt.xlabel('Year')
        #plt.ylabel('Yield(t/ha)')
        #plt.legend()
        #st.pyplot(plt)


