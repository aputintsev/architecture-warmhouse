# Используем базовый образ Python на базе Alpine
FROM python:3.8-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости и очищаем кэши
RUN apk add --no-cache gcc musl-dev linux-headers && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev linux-headers

# Определяем команду для запуска приложения
CMD ["python", "app.py"]