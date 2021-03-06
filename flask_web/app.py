from flask import Flask, render_template, request
from PIL import Image


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    try:
        image = Image.open(uploaded_file.stream)
        return f"Width: {image.width}, Height: {image.height}"
    except Exception as e:
        return f"File: {upload_file}, Exception: {e}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
