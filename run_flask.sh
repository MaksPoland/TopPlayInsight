#!/bin/bash

# Остановить любые запущенные процессы Flask
pkill -f "python app.py" || true
pkill -f "python main.py" || true

# Запуск сервера Flask на порту 8080 и привязка ко всем интерфейсам
export FLASK_APP=app.py
export FLASK_DEBUG=1
python -m flask run --host=0.0.0.0 --port=8080