FROM python:3.11-slim AS base

# Create a non-root user
RUN addgroup --gid 1000 appgroup && \
    adduser --uid 1000 --gid 1000 --disabled-password --gecos "" appuser

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source and assets
COPY app.py ./
COPY templates ./templates
COPY static ./static

USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
