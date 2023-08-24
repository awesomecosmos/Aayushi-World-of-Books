import pandas as pd
# import matplotlib.pyplot as plt

def read_books(filename):
    df = pd.read_excel(filename)
    df = df.drop_duplicates()
    df['fiction_status'] = df['fiction_status'].fillna('fiction')
    return df