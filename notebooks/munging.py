import pandas as pd

def load_data(datafile):
    data_df = pd.read_csv(datafile)
    return data_df