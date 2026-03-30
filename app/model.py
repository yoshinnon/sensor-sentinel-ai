from sklearn.ensemble import IsolationForest

def train_anomaly_detector(data, contamination=0.05):
    model = IsolationForest(contamination=contamination, random_state=42)
    return model.fit_predict(data)
