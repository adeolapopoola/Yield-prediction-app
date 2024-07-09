import streamlit as st
from multiapp import MultiApp
from apps import home, dashboards, arima, ml_models, about

app = MultiApp()

st.set_page_config(page_title='Yield prophet!', page_icon=':chart_with_upwards_trend:')

st.markdown(
        """
        <style>

        .stApp {
            background-color: #004d40;
        }

        [data-testid="stHeader"] {
            background-color: #00695c;
        }
        [data-testid="stHeader"] h1 {
            font-weight: bold;
            color: white;
        }

        [data-testid="stSidebar"] {
            background-color: #004d40;
        }
        [data-testid="stSidebarContent"] {
            background-color: #004d40;
        }
        [data-testid="stSidebarContent"] .css-145kmo2 {
            font-weight: bold;
            color: white;
        }

        .header {
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
        .content {
            font-size: 18px;
            font-weight: bold;
            color: white;
        }

        .stApp label, .stApp .stMarkdown, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
            color: white !important;
            font-weight: bold;}

            
        </style>
        """,
        unsafe_allow_html=True
    )

#st.markdown(
    #"""
    #<style>
    #.stApp {
        #background-color: #00695c;
   # }
    #</style>
    #""",
    #unsafe_allow_html=True
#)


# Add all pages here
app.add_app("Home", home.app, '🏠')
app.add_app("Dashboards", dashboards.app, '📊')
app.add_app("ARIMA Prediction", arima.app, '🔍')
app.add_app("ML Models", ml_models.app, '🤖')
app.add_app("About", about.app, '🔍' )

# Run the app
app.run()
