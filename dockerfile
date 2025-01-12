# Use an official Python image as the base
FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only the requirements file initially
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port if needed (optional; remove if not used)
# EXPOSE 5000

# Default command to run the program
CMD ["python", "main.py"]
