FROM alpine:3.7

WORKDIR /app

COPY . /app
COPY requrements.txt /app

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
