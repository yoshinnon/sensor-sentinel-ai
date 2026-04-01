import pandas as pd
import numpy as np
from app.preprocess import clean_sensor_data

def test_clean_sensor_data():
    df = pd.DataFrame({'val': [1, np.nan, 3]})
    df_cleaned = clean_sensor_data(df, 'val')
    assert df_cleaned['val'].iloc[1] == 2.0
