import pandas as pd
import streamlit as st
# import matplotlib.pyplot as plt

# IMPORTANT: Cache the conversion to prevent computation on every rerun
@st.cache_data
def read_books(filename):
    """
    Function to read an Excel file of Simplified format
    and perform basic data cleaning.

    Args:
        filename (str): Path to file.

    Returns:
        df (Pandas DataFrame): Cleaned DataFrame.
    """
    df = pd.read_excel(filename)
    df = df.drop_duplicates()
    df['fiction_status'] = df['fiction_status'].fillna('fiction')
    return df

# IMPORTANT: Cache the conversion to prevent computation on every rerun
@st.cache_data
def transform_goodreads_output(raw):
    """
    Function to transform Goodreads export to Simplified format.

    Args:
        raw (Pandas DataFrame): DataFrame of GoodReads export.

    Returns:
        raw (Pandas DataFrame): Cleaned DataFrame in Simplified format.
    """
    raw = raw.rename({'Bookshelves':'user_genre'}, axis=1)
    cols = ['Year Read','fiction_status', 'user_tags', 'ownership_status', 'buy?']
    for col in cols:
        raw[col] = np.nan
    raw['Year Read'] = raw['Date Read'].dt.year
    raw = raw.drop(['Book Id','Author', 'My Rating', 
               'Average Rating', 'Bookshelves with positions',
               'Exclusive Shelf', 'My Review', 'Spoiler', 'Private Notes',
               'Read Count', 'Owned Copies','Date Read', 'Date Added'],
               axis=1)
    raw = raw.drop_duplicates()
    return raw

def isbn_request(isbn):
    return f'https://openlibrary.org/isbn/{isbn}.json'

def extract_json(json_result, cols):
    for col in cols:
        try:
            info = json_result[col]
        except:
            print(f"Warning: '{col}' is an invalid key.")
    return info

def insert_info_into_dict(my_dict, key_name, json_result, cols):
    try:
        my_dict[key_name] = extract_json(json_result, cols)
    except:
        my_dict[key_name] = np.nan
    return my_dict