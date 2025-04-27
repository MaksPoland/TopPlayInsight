import os
from flask import Flask, render_template
from models import db, Casino, Review, Tip, Contact

# Create the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-key-for-topplayinsight")

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
if not app.config["SQLALCHEMY_DATABASE_URI"]:
    print("Warning: DATABASE_URL is not set. Using SQLite as fallback.")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///topplayinsight.db"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    featured_casinos = Casino.query.filter_by(is_featured=True).all()
    new_casinos = Casino.query.filter_by(is_new=True).all()
    all_casinos = Casino.query.all()
    return render_template('index.html', 
                          active_page='home',
                          featured_casinos=featured_casinos,
                          new_casinos=new_casinos,
                          all_casinos=all_casinos)

@app.route('/reviews')
def reviews():
    return render_template('reviews.html', active_page='reviews')

@app.route('/tips')
def tips():
    return render_template('tips.html', active_page='tips')

@app.route('/responsible-gaming')
def responsible_gaming():
    return render_template('responsible_gaming.html', active_page='responsible_gaming')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html', active_page='privacy_policy')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
