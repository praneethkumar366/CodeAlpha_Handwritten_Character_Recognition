import pandas as pd
import numpy as np

def load_data(csv_path):
    print("[INFO] Loading data...")
    data = pd.read_csv(csv_path)

    X = data.drop('0', axis=1).values  # All pixels
    y = data['0'].values               # Labels

    X = X.reshape(-1, 28, 28, 1)       # Reshape for CNN: [num_samples, 28, 28, 1]
    X = X / 255.0                      # Normalise pixel values

    return X, y
