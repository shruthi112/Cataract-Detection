from flask import Flask, request, render_template

import base64
import numpy
# import cv2
import os

UPLOAD_FOLDER = "media"

app = Flask(__name__)
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["imgdir"] = UPLOAD_FOLDER

def load_model():
    class tmp:
        def predict(x):
            print('Predicting for', x)
    
    return tmp()

MODEL = load_model()

def predict(image):
    return MODEL.predict(image)

@app.route('/upload', methods=["POST"])
def process_image():
    data = request.get_data().decode()
    image_b64 = data["image"]
    image = base64.decodebytes(image_b64)
    result = predict(image)
    return {"result": result}

@app.route('/', methods=["GET", "POST"])
def upload_image():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        data = request.files['file']
        # filename = secure_filename(file.filename) # save file 
        filename = data.filename
        filepath = os.path.join(app.config['imgdir'], filename)
        data.save(filepath)
        # img = cv2.imread(filepath)
        result = 'non-cataract' # predict(img)
        return render_template("result.html", **{"result": result})

@app.route('/home',methods=["GET","POST"])
def homepage():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        data = request.files['file']
        # filename = secure_filename(file.filename) # save file 
        filename = data.filename
        filepath = os.path.join(app.config['imgdir'], filename)
        data.save(filepath)
        # img = cv2.imread(filepath)
        result = 'non-cataract' # predict(img)
        return render_template("result.html", **{"result": result})        