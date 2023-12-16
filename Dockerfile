# Pull the latest version of the Python container.
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y python3-opencv poppler-utils

COPY . .

# Set the working directory to /app
WORKDIR .

RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]