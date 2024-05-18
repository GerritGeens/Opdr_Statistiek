import numpy as np
import matplotlib.pyplot as plt

def read_cars_data (cars_data_data_file_path): 

    # Read data the CSV file into a DataFrame
    df = pd.read_csv(cars_data_data_file_path)

    return df



def vertaal_letter_in_kleur (letter) :
    """
    translate a an input letter to an RGB channel 
    """
    letter_naar_channel = {
        'R': 0,
        'G': 1,
        'B': 2,
        'r': 0,
        'g': 1,
        'b': 2
    }

    return letter_naar_channel[letter]

