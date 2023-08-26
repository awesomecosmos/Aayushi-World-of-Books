import numpy as np  
import pandas as pd  
# import plotly.express as px  
import streamlit as st  
from utils import *

st.title("Aayushi's World of Books")

df = read_books('data/simplified_book_list.xlsx')
st.write(df)