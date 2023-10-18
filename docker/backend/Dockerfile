# Base image
FROM python:3.12-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/Pipfile .
COPY backend/Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

# Copy the Django project
COPY . /app/

# Expose the application port (if applicable)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
