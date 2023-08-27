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

fig1 = px.bar(grouped_df,
             x='Year Read',
             y='Title',
             title='Total Books Read by Year',
             labels={
                 'Year Read':'Year Read',
                 'Title':'Total Books Read'}
             )

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(
    df,
    x='Original Publication Year', 
    y='Year Read',
    title='Year I Read Books vs Year Book was Published',
    labels={
        'Year Read':'Year Read',
        'Original Publication Year':'Original Publication Year'}
    )
st.plotly_chart(fig2, use_container_width=True)
# total num of pages per year divided by 365 = avg pages read per year
# make trend line graph
# superimpose with my reading speed (online reading speed)

# compoare book marketing trends vs when i read them
# properly capitilze words