from tensorflow.keras.models import load_model
import numpy as np
import cv2

model = load_model("models/character_model.h5")

def predict_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28)) / 255.0
    img = img.reshape(1, 28, 28, 1)

    pred = model.predict(img)
    label = np.argmax(pred)

    return chr(label + 65)  # 0 = A, 1 = B, ...
