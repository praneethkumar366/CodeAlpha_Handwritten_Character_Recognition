import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from tensorflow.keras.models import load_model

# Load the model
model = load_model("C:/Users/PRANEETH/OneDrive/Desktop/Placement Material/Projects/Handwritten_Character_Recognition/models/handwritten_model.h5")

class HandwritingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("🖊️ Handwritten Character Recognition")
        self.geometry("500x600")
        self.configure(bg="#f0f8ff")
        self.resizable(False, False)

        self.predicted_sentence = ""

        tk.Label(self, text="Draw an Alphabet", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#2c3e50").pack(pady=10)

        self.canvas = tk.Canvas(self, width=280, height=280, bg="white", borderwidth=3, relief="ridge")
        self.canvas.pack(pady=10)

        self.image = Image.new("L", (280, 280), color=255)
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        button_frame = tk.Frame(self, bg="#f0f8ff")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Predict & Add", font=("Arial", 12), bg="#27ae60", fg="white", command=self.predict).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Clear Drawing", font=("Arial", 12), bg="#c0392b", fg="white", command=self.clear_canvas).grid(row=0, column=1, padx=5)

        action_frame = tk.Frame(self, bg="#f0f8ff")
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="Space", font=("Arial", 12), command=self.add_space).grid(row=0, column=0, padx=5)
        tk.Button(action_frame, text="Backspace", font=("Arial", 12), command=self.backspace).grid(row=0, column=1, padx=5)
        tk.Button(action_frame, text="Clear Sentence", font=("Arial", 12), command=self.clear_sentence).grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(self, text="Predicted: ", font=("Arial", 16), bg="#f0f8ff", fg="#34495e")
        self.result_label.pack(pady=5)

        self.sentence_label = tk.Label(self, text="Sentence: ", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#2c3e50", wraplength=450, justify="center")
        self.sentence_label.pack(pady=10)

    def paint(self, event):
        x, y = event.x, event.y
        r = 8
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill=0)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 280, 280], fill=255)
        self.result_label.config(text="Predicted: ")

    def clear_sentence(self):
        self.predicted_sentence = ""
        self.sentence_label.config(text="Sentence: ")

    def backspace(self):
        self.predicted_sentence = self.predicted_sentence[:-1]
        self.sentence_label.config(text="Sentence: " + self.predicted_sentence)

    def add_space(self):
        self.predicted_sentence += " "
        self.sentence_label.config(text="Sentence: " + self.predicted_sentence)

    def predict(self):
        img = self.image.resize((28, 28))
        img = ImageOps.invert(img)
        img = np.array(img).astype("float32") / 255.0
        img = img.reshape(1, 28, 28, 1)

        prediction = model.predict(img)
        index = np.argmax(prediction)
        character = chr(index + 65)  # Assuming A-Z
        confidence = prediction[0][index] * 100

        self.result_label.config(text=f"Predicted: {character} ({confidence:.2f}%)")
        self.predicted_sentence += character
        self.sentence_label.config(text="Sentence: " + self.predicted_sentence)

        self.clear_canvas()  # Clear after predicting

if __name__ == "__main__":
    app = HandwritingApp()
    app.mainloop()
