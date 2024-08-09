import streamlit as st
import pandas as pd
import joblib
import pickle

timeseries_df = pd.read_csv(r"C:\Users\deola\Downloads\Dashboard_data (1).xls", parse_dates=['Year'])
timeseries_df.set_index('Year', inplace=True)

xgboost_model = pickle.load(open('boost.pkl', 'rb'))
#knr_model = joblib.load('knr.pkl')
nn_model = joblib.load('nn.pkl')
preprocessor = joblib.load('preprocessor.pkl')

#Function to calculate country-specific quartiles
def calculate_country_quartiles(df, country):
    country_df = df[df['Country'] == country]
    quartiles = {}
    for var in ['AverageTemperature', 'Average precipitation in depth (mm per year)', 'Nitrogen(t/ha)']:
        q1 = country_df[var].quantile(0.25)
        q3 = country_df[var].quantile(0.75)
        quartiles[var] = (q1, q3)
    return quartiles


def predict_xgboost(features):
    transformed_features = preprocessor.transform(features)
    predicted_value = xgboost_model.predict(transformed_features)
    return predicted_value

#def predict_knr(features):
    #transformed_features = preprocessor.transform(features)
    #predicted_value = knr_model.predict(transformed_features)
    #return predicted_value

def predict_nn(features):
    transformed_features = preprocessor.transform(features)
    predicted_value = nn_model.predict(transformed_features)
    return predicted_value

def app():
    st.subheader('Predictions with Machine Learning Models')
    model = st.selectbox('Select Model', ['Neural Networks', 'XGBoost'])#'K-Nearest Neighbors'
    Country = st.selectbox('Select Country', timeseries_df['Country'].unique())
    Crop_type = st.selectbox('Select Crop Type', timeseries_df['Crop_type'].unique())
    quartiles = calculate_country_quartiles(timeseries_df, Country)
    
    # Get ranges for the selected country
    temp_q1, temp_q3 = quartiles['AverageTemperature']
    precip_q1, precip_q3 = quartiles['Average precipitation in depth (mm per year)']
    nitrogen_q1, nitrogen_q3 = quartiles['Nitrogen(t/ha)']
    
    # Selecting categories instead of numerical inputs
    Avg_precipitation_cat = st.selectbox('Select Average Rainfall Category', ['Low', 'Medium', 'High'])
    Avg_temperature_cat = st.selectbox('Select Average Temperature Category', ['Low', 'Medium', 'High'])
    Nitrogen_t_ha_cat= st.selectbox('Select Fertilizer Input Category (Nitrogen)', ['Low', 'Medium', 'High'])

    Year = st.slider('Select Year',
        min_value=int(timeseries_df.index.year.min()),
        max_value=2030,
        step=1)

    if st.button('Predict Yield'):
        # Convert categories to country-specific numerical ranges for model input
        def category_to_value(category, q1, q3):
            if category == 'Low':
                return q1 - 1  # Slightly below Q1
            elif category == 'Medium':
                return (q1 + q3) / 2
            elif category == 'High':
                return q3 + 1  # Slightly above Q3
            else:
                return None
        
        Avg_precipitation = category_to_value(Avg_precipitation_cat, precip_q1, precip_q3)
        Avg_temperature = category_to_value(Avg_temperature_cat, temp_q1, temp_q3)
        Nitrogen_t_ha = category_to_value(Nitrogen_t_ha_cat, nitrogen_q1, nitrogen_q3)
        
       # Create features DataFrame 
        features = pd.DataFrame([[Year, Country, Crop_type, Avg_precipitation, Avg_temperature, Nitrogen_t_ha]],
                                columns=['Year', 'Country', 'Crop_type', 'Averageprecipitation_mm_per_yr', 'AverageTemperature', 'Nitrogen_t_ha'])
        if model == 'XGBoost':
            predicted_yield_xgb = predict_xgboost(features)
            st.write(f"Predicted yield for {Crop_type} in {Country} for {Year}: {predicted_yield_xgb[0]:.4f}(t/ha)")
        
        #elif model == 'K-Nearest Neighbors':
            #predicted_yield_knr = predict_knr(features)
            #st.write(f"Yield prediction for {Crop_type} in {Country} for {Year}: {predicted_yield_knr[0]:.4f}(t/ha)")
            
        elif model == 'Neural Networks':
            predicted_yield_nn = predict_nn(features)
            st.write(f"Yield prediction for {Crop_type} in {Country} for {Year}: {predicted_yield_nn[0].item():.4f}(t/ha)")
