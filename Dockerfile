FROM tensorflow/tensorflow:latest-py3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
add . /code/
EXPOSE 3000
cmd python manage.py migrate && python manage.py runserver 0.0.0.0:8000
