import pandas as pd
# import matplotlib.pyplot as plt

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