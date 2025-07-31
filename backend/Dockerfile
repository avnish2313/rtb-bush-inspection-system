FROM python:3.11-slim AS base

# Create a user for running the app – this avoids running as root in the
# container which is considered a best practice. We choose UID/GID 1000
# because it's commonly available on Linux systems but any non-zero value is fine.
RUN addgroup --gid 1000 appgroup && \
    adduser --uid 1000 --gid 1000 --disabled-password --gecos "" appuser

# Set up working directory
WORKDIR /app

# Copy dependency definitions first for separate caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY app.py .

# Use an unprivileged user to run the application
USER appuser

# Expose the port the backend listens on
EXPOSE 5000

# Entrypoint to run the service
CMD ["python", "app.py"]
