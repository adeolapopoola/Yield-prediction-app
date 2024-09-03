import streamlit as st
def app():
    st.subheader ('About Yield Prophet App')
    st.write(
        '''Welcome to the Yield Prophet App! This application uses advanced machine learning models to predict crop yields based on historical data, environmental factors, and crop-specific parameters. Whether you're a farmer, agricultural researcher, or just curious, my goal is to provide accurate predictions to support decision-making and enhance productivity in agriculture.

**Features**: 
This app harnesses the power of advanced machine learning algorithms to forecast crop yields with high accuracy. Here are some of the key features:

**Predictive Models**:
- ARIMA Model: Uses the Autoregressive Integrated Moving Average model for time series forecasting.
- Neural Networks(R²= 0.93): Utilizes deep learning techniques to predict complex patterns in crop yield data.
- XGBoost (89%): Uses extreme gradient boosting for efficient and accurate predictions.

**Interactive Visualization**: 
Visualize trends and predicted yields with interactive and user-friendly visualizations.
**Customizable Inputs**: 
Allows users to input parameters such as weather conditions to tailor predictions.

**Data**: 
This app contains data for about 150 countries and 296 crops.


**Data Sources**:
- Food and Agricultural Organisation (https://www.fao.org/faostat/en/#data)
- Our World in Data (https://ourworldindata.org)
- Kaggle (https://www.kaggle.com/datasets)



**Feedback**:
Your feedback is valuable to me! If you have suggestions or encounter any issues while using the app, please reach out to me via email at deolapopson@gmail.com


Thank you for using the Yield Prophet App!
''')
