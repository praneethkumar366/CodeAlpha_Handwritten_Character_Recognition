from data_loader import load_data
from model import create_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint
import os

# Load and split data
X, y = load_data("C:/Users/PRANEETH/OneDrive/Desktop/Placement Material/Projects/Handwritten_Character_Recognition/data/A_Z Handwritten Data.csv")
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1)

# Create model
model = create_model()

# Train and save model
if not os.path.exists("models"):
    os.makedirs("models")

checkpoint = ModelCheckpoint("models/character_model.h5", save_best_only=True)
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val), callbacks=[checkpoint])
