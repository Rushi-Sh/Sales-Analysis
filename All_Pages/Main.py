import os
import pandas as pd
import numpy as np

import streamlit as st
from streamlit_option_menu import option_menu 

st.set_page_config(
    page_title="Home Page",
    page_icon="home.png",
    layout="wide"
)


import Page1,Page2

with st.sidebar:
    selected = option_menu("Main Menu", ["Databases", 'Dashboard'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)
    
if selected == "Databases":
    Page1.app()
if selected == "Dashboard":
    Page2.app()    
   



        

