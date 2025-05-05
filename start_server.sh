#!/bin/bash

# Остановить любые запущенные процессы Flask
pkill -f "python app.py" || true
pkill -f "python main.py" || true
pkill -f "flask run" || true

# Запуск сервера Flask на порту 8080 и привязка ко всем интерфейсам
export FLASK_APP=app.py
export FLASK_DEBUG=1

# Запуск в фоновом режиме
python -m flask run --host=0.0.0.0 --port=8080 > flask.log 2>&1 &
SERVER_PID=$!

echo "Flask сервер запущен с PID: $SERVER_PID"
echo "Доступен по адресу: http://localhost:8080"
echo "Для остановки сервера выполните: kill $SERVER_PID"