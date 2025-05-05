from app import app
from models import Casino

with app.app_context():
    casinos = Casino.query.all()
    for casino in casinos:
        print(f"Casino: {casino.name}")
        print(f"Bonus: {casino.bonus_description}")
        print("---")