# ✍️ Handwritten Character Recognition with Tkinter GUI

A Python-based Handwritten Character Recognition system using a Convolutional Neural Network (CNN) model trained on English alphabets. This app allows users to draw characters on a canvas and predicts them with high accuracy. The GUI is built using **Tkinter** with a sleek and modern design.

---

## 🚀 Features

- 🎨 Intuitive canvas to draw characters (A–Z)
- 🔍 Real-time prediction with confidence score
- 🧠 CNN-based trained model (Keras + TensorFlow)
- ⌨️ Full sentence builder with:
  - Space
  - Backspace
  - Clear All
- 💡 Beginner-friendly clean codebase
- 🎯 Responsive and visually appealing UI



## 📸 Screenshots

![image](https://github.com/user-attachments/assets/bb3ee2d2-9f3d-4819-84ba-b867bbb11da1)


## 🛠️ Requirements

- Python 3.8+
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Tkinter (built-in)

Install dependencies with:
pip install -r requirements.txt

🧪 How to Run
Clone the repository:
git clone https://github.com/yourusername/handwritten-character-recognition.git
cd handwritten-character-recognition

Activate your virtual environment or create one:
python -m venv venv
venv\Scripts\activate  # On Windows

Install dependencies:
pip install -r requirements.txt
Run the application:
cd gui
python app.py

📁 Note on Virtual Environment
To keep the repo lightweight, the virtual environment (venv/) is excluded and/or compressed. It is recommended to create your own environment as shown above.

🤖 Model Info
The character_model.h5 is a trained CNN on grayscale 28x28 character images (A–Z). You can retrain or update the model in the /models folder.

📌 Project Structure
Copy
Edit
Handwritten_Character_Recognition/
│
├── gui/
│   └── app.py
├── models/
│   └── character_model.h5
├── requirements.txt
└── README.md
👨‍🎓 Author
Praneeth
B.Tech CSE (Data Science) | ML Enthusiast | Frontend & Backend Developer
LinkedIn | GitHub

⭐️ Give a Star!
If you found this project helpful or inspiring, consider giving it a ⭐️ to support the work!
