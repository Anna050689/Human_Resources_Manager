FROM python:3.8.8-buster

# Make directory for the application
WORKDIR /app

# Install dependencies
COPY requirements.txt
RUN pip install -r requirements.txt

# Copy the source code
COPY /app .
CMD ["python", "main.py"]
