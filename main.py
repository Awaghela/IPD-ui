import streamlit as st
import pandas as pd
import utils as utl
from multiapp import MultiApp
from apps import app1, app2, app3, app4
app = MultiApp()


st.set_page_config(layout="wide", page_title='Navbar sample')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

app.add_app("Auto ML dataset explorer", app1.app)
app.add_app("AutoML of Regression models", app2.app)
app.add_app("AutoML of Classification models", app3.app)
app.add_app("The Machine Learning Hyper parameter Optimization App", app4.app)
# The main app
app.run()


def navigation():
    route = utl.get_current_route()
    if route == "Auto ML dataset explorer":
        app1.load_view()
    elif route == "AutoML of Regression models":
        app2.load_view()
    elif route == "AutoML of Classification models":
        app3.load_view()
    elif route == "The Machine Learning Hyper parameter Optimization App":
        app4.load_view()
navigation()