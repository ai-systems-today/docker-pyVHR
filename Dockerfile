FROM python:3.8

RUN apt-get update && apt-get install -y cmake gfortran ffmpeg libsm6 libxext6

WORKDIR /app

COPY requirements.txt /app/
RUN pip install numpy
RUN pip install -r requirements.txt

COPY requirements_dev.txt /app/
RUN pip install -r requirements_dev.txt

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]