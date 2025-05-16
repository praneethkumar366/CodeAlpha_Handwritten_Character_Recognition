# train_model.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Load dataset
data = pd.read_csv("C:/Users/PRANEETH/OneDrive/Desktop/Placement Material/Projects/Handwritten_Character_Recognition/data/A_Z Handwritten Data.csv").astype("float32")

# Separate features and labels
X = data.drop("0", axis=1)
y = data["0"]

# Normalize the data
X = X / 255

# Reshape the images to 28x28 pixels
X = X.values.reshape(-1, 28, 28, 1)

# One-hot encode labels
y = to_categorical(y, num_classes=26)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Define the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(26, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=256)

# Save model
model.save("handwritten_model.h5")
