[run_flask]
command = "python -m flask run --host=0.0.0.0 --port=8080"
env = { FLASK_APP = "app.py", FLASK_ENV = "development", FLASK_DEBUG = "1" }