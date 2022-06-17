import streamlit as st  # type:ignore
import requests

baseREMOTEURL = "https://montegure.deta.dev/basic"
baseLocalURL = "http://192.168.5.246:5000/basic"
st.write("test")
data = requests.get(baseREMOTEURL+"/users").json()
st.write(data)
