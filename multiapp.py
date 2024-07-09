import streamlit as st
from streamlit_option_menu import option_menu

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func, icon):
        self.apps.append({
            "title": title,
            "function": func,
            "icon": icon
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title = None,
                options = ['Home', 'Dashboards','ARIMA Prediction', 'ML Models', 'About'],
                icons = ['house-fill', 'bar-chart-fill','graph-up-arrow', 'robot', 'info-circle-fill'],
                default_index = 0,
                styles ={'container':{'padding':'4!important', 'background-color':'#004d40'},
                         'icon':{'color':'white'},
                         'menu_icon':'cast',
                         'nav-link':{'color':'white', "--hover-color": '#00695c'},
                         'nav-link-selected':{'background-color':'#00695c'}}
            )
        for app_item in self.apps:
            if app == app_item['title']:
                app_item['function']()

