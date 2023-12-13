# Pull the latest version of the Python container.
FROM python:3.8-slim-buster

COPY app/ /app

# Set the working directory to /app
WORKDIR /app

RUN python -m pip install -r requirements.txt

EXPOSE 8500

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8500"]