import os
from flask import Flask, render_template, request, flash, redirect, url_for
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
    # Get featured casinos, sorted by rating from highest to lowest
    featured_casinos = Casino.query.filter_by(is_featured=True).order_by(Casino.rating.desc()).all()
    new_casinos = Casino.query.filter_by(is_new=True).all()
    all_casinos = Casino.query.order_by(Casino.rating.desc()).all()
    return render_template('index.html', 
                          active_page='home',
                          featured_casinos=featured_casinos,
                          new_casinos=new_casinos,
                          all_casinos=all_casinos)

@app.route('/reviews')
def reviews():
    casino_reviews = Review.query.all()
    casinos = Casino.query.all()
    return render_template('reviews.html', 
                          active_page='reviews',
                          casino_reviews=casino_reviews,
                          casinos=casinos)

@app.route('/tips')
def tips():
    all_tips = Tip.query.all()
    return render_template('tips.html', 
                          active_page='tips', 
                          tips=all_tips)

@app.route('/responsible-gaming')
def responsible_gaming():
    return render_template('responsible_gaming.html', active_page='responsible_gaming')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Validate form data
        if not name or not email or not subject or not message:
            flash('All fields are required!', 'danger')
            return render_template('contact.html', active_page='contact')
        
        # Create new contact record
        new_contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Save to database
        db.session.add(new_contact)
        db.session.commit()
        
        # Show success message
        flash('Your message has been sent successfully! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', active_page='contact')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html', active_page='privacy_policy')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
