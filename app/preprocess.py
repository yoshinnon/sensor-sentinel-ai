import pandas as pd

def clean_sensor_data(df, column):
    # 欠損値の線形補完
    df[column] = df[column].interpolate(method='linear')
    return df
