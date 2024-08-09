import streamlit as st

def app():
    st.markdown(
        """
        <style>
        [data-testid = 'stAppViewContainer']{
        background-image:url('https://github.com/adeolapopoola/Yield-prediction-app/blob/main/Agri-LL_Square.jpg?raw=true');
        background-size: 95%;
        background-position: center;
        background-repeat: no-repeat;
        }

        [data-testid = 'stHeader']{
        background-color: #00695c;
        }

        [data-testid = 'stHeader'] h1 {
        font-weight: bold;
        color: white;
        }

        [data-testid = 'stSidebarContent']{
        background-color: #00695c;
        }

        .header {
            font-size: 3em; 
            font-weight: bold; 
            color: white;  
            text-align: center;  
            margin-top: 20px;  
            text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);  
        }

        .content {
            font-size: 1.5em;  
            color: white;  
            text-align: center;  
            margin-bottom: 30px;  
        }
  
        </style>
        """,
        unsafe_allow_html=True
    )


    
    st.markdown('<p class="header">Welcome to the Yield Prophet App!</p>', unsafe_allow_html=True)
    st.markdown('<div class="content">This app allows you to predict yield using various models.</div>', unsafe_allow_html=True)
