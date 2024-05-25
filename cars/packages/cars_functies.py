import pandas as pd

def read_cars_data(cars_data_data_file_path): 

    # Read data the CSV file into a DataFrame
    df = pd.read_csv(cars_data_data_file_path)

    return df

