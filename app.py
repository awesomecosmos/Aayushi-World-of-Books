import numpy as np  
import pandas as pd  
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyo
import streamlit as st  
from pandas.api.types import is_categorical_dtype,is_datetime64_any_dtype,is_numeric_dtype,is_object_dtype
from code.utils import *

st.title("Aayushi's World of Books :books: :sparkles:")

tab1, tab2, tab3 = st.tabs(["Home","Graphs","Data"])

with tab1:
    st.header('About This Project')
    about = '''
    I have always been a voracious reader, and will read anything in sight. Over the years, I have read a 
    plethora of books, and it recently occurred to me that it would be nice to have records of everything I've read.
    This app is the result, and the hope is to catalogue and keep track of all the books I've read, and 
    graphically show simple statistics and charts about my reading habits. 

    Click on the tabs above to explore!
    '''
    st.markdown(about)

    st.header('Motivation')
    motivation = '''
    One of my earliest memories of trying to cultivate a personal library is when I was 6
    and I started putting all my books into a box and creating custom library cards to stick 
    at the back of the book to keep track of when my little sister took my books to play with.
    That system tragically did not work, but I continued to amass more books as the years went by.
    I lost a lot of my childhood books during several house moves, but am now beginning to rebuild
    my personal library. As of September 2023, I have close to 75 physical books on my bookshelf,
    but it is my deepest ambition to have a large personal library. This app is my attempt at recording 
    metadata about books I own physically, digitally, and which I've borrowed.
    '''
    st.markdown(motivation)
    img1 = '/Users/aayushiverma/Documents/Github/My-Book-Stats/assets/interstellar.jpeg'
    img1_caption = 'One of my motivations is Murph\'s bookshelf in Interstellar (2014), which played a key role in the movie and kind of saved the universe. I don\'t think my bookshelf can do that, but one can dream.'
    st.image(img1, caption=img1_caption)
    
    st.header('My Actual Bookshelf')
    st.write('Image of my actual bookshelf coming soon!')
    # img2 = 'path'
    # st.image(img2, caption='My real bookshelf as of Sep. 2023.')

with tab2:
    df = read_books('data/simplified_book_list.xlsx')
    grouped_df = df.groupby(['Year Read']).count().reset_index()

    fig1 = px.bar(grouped_df,
                x='Year Read',
                y='Title',
                title='Total Books Read by Year',
                color_discrete_sequence=['blueviolet'],
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
        color_discrete_sequence=['blueviolet'],
        labels={
            'Year Read':'Year Read',
            'Original Publication Year':'Original Publication Year'}
        )
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    df = read_books('data/simplified_book_list.xlsx')
    st.dataframe(filter_dataframe(df))  