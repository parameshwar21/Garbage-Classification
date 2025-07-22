from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("model/waste_classifier_model.keras")
classes = ['glass', 'metal','plastic']

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    filename = None

    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join("static/uploaded", file.filename)
            file.save(filepath)
            img = image.load_img(filepath, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0
            prediction = classes[np.argmax(model.predict(img_array))]
            filename = file.filename

    return render_template("index.html", prediction=prediction, filename=filename)
    
if __name__ == "__main__":
    app.run(debug=True)
