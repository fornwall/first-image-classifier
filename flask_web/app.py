from flask import Flask, render_template, request
# from PIL import Image
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
        prediction = learner.predict(temp.name)
        predicted_category = prediction[0] # 'yes' or 'no'
        predicted_category_idx = list(learner.dls.vocab).index(predicted_category)
        certainty = prediction[2][predicted_category_idx]

        return f"Smiling: {prediction[0]} (with {certainty} certainty)"
    except Exception as e:
        return f"File: {upload_file}, Exception: {e}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
