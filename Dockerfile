# FROM python:3.9-slim
# COPY requirements.txt requirements.txt
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . /app
# WORKDIR /app
# EXPOSE 8080
# ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0 --port=8080


FROM python:3.9-slim-buster


RUN apt-get update && apt-get install -y python3-dev build-essential

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "app:app"]

