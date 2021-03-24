# A deep learning image classifier web application
A small web application created following the [From Model to Production](https://github.com/fastai/fastbook/blob/master/02_production.ipynb) chapter of [the fastai book](https://github.com/fastai/fastbook).

- The model is trained as shown in [notebook.ipynb](notebook.ipynb).
- Faces are from the [UTKFace](https://susanqq.github.io/UTKFace/) Large Scale Face Dataset.
- A web app using the [Flask](https://flask.palletsprojects.com/) framework in the [flask_web/](flask_web/) directory exposes the model.
- Using [Dockerfile](flask_web/Dockerfile) a [docker image](https://hub.docker.com/r/fredrikfornwall/first-image-classifier) is built.
- The image is deployed using [fly.io](https://fly.io) to [https://image-classifier.fly.dev/](https://image-classifier.fly.dev/).
