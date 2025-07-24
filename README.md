# 🗑️ Garbage Classification using Python and HTML

This project is a Deep Learning-based image classification system that categorizes garbage into different classes such as **Plastic**, **Glass**, **Paper**, etc. It helps promote smart waste management and recycling by identifying the type of waste based on images.

---

## 🔍 Overview

Garbage classification plays a crucial role in environmental sustainability. This system uses a Convolutional Neural Network (CNN) model trained on a custom dataset of garbage images to predict the type of waste.

---

## 📁 Dataset Structure

The dataset is divided into training and testing sets:


dataset/
├── train/
│ ├── plastic/
│ ├── glass/
│ └── metal/

└── test/
├── plastic/
├── glass/
|└── metal/




## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- OpenCV
- Matplotlib
- Flask (for deployment)
- Google Colab (for training)

---

## 🚀 Features

- Image preprocessing and data augmentation
- Custom CNN model for image classification
- Trained with high accuracy
- Web interface to upload and predict garbage class
- Exported `.h5` model for future use




## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parameshwar21/garbage-classification.git
   cd garbage-classification

2.Create a virtual environment (optional but recommended):

     python -m venv tf-venv
     tf-venv\Scripts\activate
3.Install dependencies:

    pip install -r requirements.txt

4.Run the flask app:

    python app.py

