FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
