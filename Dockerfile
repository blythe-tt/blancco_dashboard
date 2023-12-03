FROM python:3.10.12-alpine3.18
RUN apk add --no-cache tzdata
ENV TZ=Europe/London

WORKDIR /code/src

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["gunicorn","-b 0.0.0.0:5005", "warehouse_service:app", "-w 1",  "-k uvicorn.workers.UvicornWorker"]
