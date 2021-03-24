[![CI](https://github.com/fornwall/first-image-classifier/actions/workflows/ci.yml/badge.svg)](https://github.com/fornwall/first-image-classifier/actions/workflows/ci.yml)

# A deep learning image classifier web application
A small web application created following the [From Model to Production](https://github.com/fastai/fastbook/blob/master/02_production.ipynb) chapter of [the fastai book](https://github.com/fastai/fastbook).

- A model to classify images as smiling or not is trained in [notebook.ipynb](notebook.ipynb).
- Facial images used for training and validation are from the [UTKFace](https://susanqq.github.io/UTKFace/) Large Scale Face Dataset.
- A web app using the [Flask](https://flask.palletsprojects.com/) framework in the [flask_web/](flask_web/) directory exposes the model.
- Using [Dockerfile](flask_web/Dockerfile) a [docker image](https://hub.docker.com/r/fredrikfornwall/first-image-classifier) is built.
- The image is deployed using [fly.io](https://fly.io) to [https://image-classifier.fly.dev/](https://image-classifier.fly.dev/).
- The build and deployment is done on pushes to the main branch by [a Github CI workflow](.github/workflows/ci.yml).
