FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    openjdk-17-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt \
    faststream[rabbit] \
    pydantic-settings \
    pyspark \
    tinkoff-investments \
    numpy \
    scipy

# Копирование исходного кода
COPY . .

# Создание непривилегированного пользователя
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "web.src.main:app", "--host", "0.0.0.0", "--port", "8000"]