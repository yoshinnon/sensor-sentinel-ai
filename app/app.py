import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="Sensor Sentinel AI", layout="wide")
st.title("🛰️ Sensor Sentinel: 汎用異常検知デモ")

# パラメータ設定
contamination = st.sidebar.slider("異常値の想定割合", 0.01, 0.20, 0.05)
uploaded_file = st.file_uploader("CSVアップロード", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    time_idx = pd.date_range("2026-03-30", periods=500, freq="5min")
    vals = np.sin(np.linspace(0, 10, 500)) + np.random.normal(0, 0.1, 500)
    vals[100:105] += 2.5
    df = pd.DataFrame({"timestamp": time_idx, "value": vals})

model = IsolationForest(contamination=contamination, random_state=42)
df['is_anomaly'] = model.fit_predict(df[['value']])
df['is_anomaly'] = df['is_anomaly'].apply(lambda x: "異常" if x == -1 else "正常")

st.line_chart(df.set_index('timestamp')['value'])
st.write(df.head())
