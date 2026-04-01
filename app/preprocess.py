import pandas as pd


def clean_sensor_data(df, column):
    # pandas 3.0 対応: object-dtype を数値に変換してから線形補完
    df[column] = pd.to_numeric(df[column], errors='coerce').interpolate(method='linear')
    return df
