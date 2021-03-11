FROM python:3.9-slim

MAINTAINER Fredrik Fornwall "fredrik@fornwall.net"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt \
  && rm -Rf /root/.cache

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

