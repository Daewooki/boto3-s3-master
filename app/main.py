import boto3
import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()
"""
connect to S3
"""
client_s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key
)

@app.get(path="/")
def index():
    return "AWS S3 Access with Python Boto3."



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
