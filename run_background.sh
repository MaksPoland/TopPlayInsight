#!/bin/bash

# Остановить любые запущенные процессы Flask
pkill -f "python app.py" || true
pkill -f "python main.py" || true
pkill -f "flask run" || true

# Запуск сервера Flask в фоновом режиме
export FLASK_APP=app.py
export FLASK_DEBUG=1
python -m flask run --host=0.0.0.0 --port=8080 > flask.log 2>&1 &

echo "Сервер запущен в фоновом режиме на порту 8080"
echo "PID: $!"