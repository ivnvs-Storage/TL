FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    openjdk-17-jre-headless \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    faststream[rabbit] \
    pydantic-settings \
    pyspark

COPY pps ./pps
COPY sge ./sge
COPY .env .

ENV PYTHONPATH=/app

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "sge/consumer.py"] 