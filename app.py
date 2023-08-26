import numpy as np  
import pandas as pd  
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyo
import streamlit as st  
from utils import *

st.title("Aayushi's World of Books :books: :sparkles:")

with st.expander("Expand to see data! :open_book:"):
    df = read_books('data/simplified_book_list.xlsx')
    st.dataframe(df)
    
df = read_books('data/simplified_book_list.xlsx')
grouped_df = df.groupby(['Year Read']).count().reset_index()

fig = px.bar(grouped_df,
             x='Year Read',
             y='Title',
             title='Total Books Read by Year',
             labels={
                 'Year Read':'Year Read',
                 'Title':'Total Books Read'}
             )

st.plotly_chart(fig, use_container_width=True)