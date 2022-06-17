import streamlit as st  # type:ignore
import requests
from utils.utils import *
from manage_user.loadUserFrame import *

# command: streamlit run app.py

def hide_menu(st):
    
    hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}    
            header {visibility: hidden;}
            footer {visibility: hidden;}
            
            footer:after {
                content:'Projet OMER'; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: gray;
                padding: 5px;
                top: 2px;
            }       
               
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
def main():
    st.set_page_config(
        page_title="Nanpson REST client test",
        page_icon="🧊",
        initial_sidebar_state="collapsed"
    )
    #hide footer and header
    hide_menu(st=st)
    #side menu
    radio_value = st.sidebar.radio("Available Applications", tuple(t.value for t in listMenu))
    
    if radio_value==listMenu.users.value:        
        loadWindow(st=st)
    
    
    #st.write("test")
    
    #st.write(data)

if __name__ == '__main__':
    main()

