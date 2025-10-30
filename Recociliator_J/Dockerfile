# Python slim image
FROM python:3.12-slim

# Prevent .pyc, set non-interactive
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Workdir
WORKDIR /app

# System deps (build + runtime)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Django settings expect collectstatic in production; safe to run here too
RUN mkdir -p /app/staticfiles && \
    python manage.py collectstatic --noinput || true

# Expose port (Railway will map dynamically)
EXPOSE 8000

# Copy startup script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Use startup script as default command
CMD ["/app/start.sh"]
# Use Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY Recociliator_J/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY Recociliator_J/ .

# Copy the start script and make it executable
COPY Recociliator_J/start.sh ./start.sh
RUN chmod +x ./start.sh

# Expose the port that the platform will bind (Railway sets $PORT at runtime)
EXPOSE 8080

# Use the start script as the container entrypoint. Railway's startCommand will
# call the script (or the container default will execute it), which runs
# migrations/collectstatic then execs gunicorn bound to $PORT.
ENTRYPOINT ["./start.sh"]