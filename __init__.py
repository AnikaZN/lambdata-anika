'''
lambdata-anika - A collection of data science helper functions
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

ZEROS = np.zeros(5)
ONES = np.ones(10)

def train_validation_test_split(
    x,y, train_size = 0.7, val_size = 0.1, test_size = 0.2, random_state = 42,
    shuffle = True):

    assert train_size + val_size + test_size == 1

    x_train_val, x_test, y_train_val, y_test = train_test_split(
        x, y, test_size = test_size, random_state = random_state,
        shuffle = shuffle)

    x_train, x_val, y_train, y_val = train_test_split(
        x_train_val, y_train_val, test_size = val_size/(train_size+val_size),
        random_state = random_state, shuffle = shuffle)

    return x_train, x_val, x_test, y_train, y_val, y_test
