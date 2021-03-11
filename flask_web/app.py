from flask import Flask, render_template, request
from PIL import Image
from tempfile import NamedTemporaryFile
from fastai.learner import load_learner

# https://stackoverflow.com/questions/12984426/python-pil-ioerror-image-file-truncated-with-big-images
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


app = Flask(__name__)
learner = load_learner("model.pkl")


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    temp = NamedTemporaryFile()
    uploaded_file.save(temp)
    try:
        #image = Image.open(uploaded_file.stream)
        #image = Image.open(temp.name)
        #return f"Width: {image.width}, Height: {image.height}"
        prediction = learner.predict(temp.name)
        return f"Prediction: {prediction}"
    except Exception as e:
        return f"File: {upload_file}, Exception: {e}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
