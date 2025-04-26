import os
from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-key-for-topplayinsight")

# Routes
@app.route('/')
def index():
    return render_template('index.html', active_page='home')

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
