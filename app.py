import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.middleware.proxy_fix import ProxyFix
from models import db, Casino, Review, Tip, Contact

# Create the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-key-for-topplayinsight")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1) # needed for url_for to generate with https

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
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

# Utility function for processing bonus descriptions
def process_casino_bonus(casino):
    # Split the bonus description for display
    bonus_desc = casino.bonus_description
    bonus_text = bonus_desc.split(':', 1)[1].strip() if ':' in bonus_desc else bonus_desc
    
    # Set main bonus (everything before the + sign)
    casino.main_bonus = bonus_text.split('+')[0].strip()
    
    # Set extra bonus (everything after the + sign if it exists)
    if '+' in bonus_text:
        casino.extra_bonus = bonus_text.split('+', 1)[1].strip()
    else:
        casino.extra_bonus = None
    
    return casino

# Routes
@app.route('/')
def index():
    featured_casinos = Casino.query.filter_by(is_featured=True).all()
    new_casinos = Casino.query.filter_by(is_new=True).all()
    all_casinos = Casino.query.all()
    
    # Process all casino bonus descriptions
    for casino in featured_casinos:
        process_casino_bonus(casino)
    
    for casino in new_casinos:
        process_casino_bonus(casino)
        
    for casino in all_casinos:
        process_casino_bonus(casino)
    
    tips = Tip.query.order_by(Tip.published_date.desc()).all()
    return render_template('index.html', 
                          active_page='home',
                          featured_casinos=featured_casinos,
                          new_casinos=new_casinos,
                          all_casinos=all_casinos,
                          tips=tips)

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
        new_contact = Contact()
        new_contact.name = name
        new_contact.email = email
        new_contact.subject = subject
        new_contact.message = message
        
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
    app.run(host='0.0.0.0', port=5000, debug=True)
