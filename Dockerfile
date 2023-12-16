# Pull the latest version of the Python container.
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-opencv poppler-utils

COPY app/ /app

COPY tests/ /app

# Set the working directory to /app
WORKDIR /app

RUN python -m pip install -r requirements.txt

RUN python -m pytest .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]