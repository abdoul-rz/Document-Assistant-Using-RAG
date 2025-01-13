# Use an official Python image as the base
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /rag_app

# Copy only the requirements file initially
COPY requirements.txt /rag_app/

# Install the dependencies
RUN pip install --upgrade pip --verbose && \
    pip install -r requirements.txt --verbose

# Copy the rest of the application code
COPY . /rag_app/

# Default command to run the program
CMD ["python", "main.py"]
