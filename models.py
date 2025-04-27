from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Casino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo_url = db.Column(db.String(255))
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False, default=0.0)
    bonus_description = db.Column(db.String(255))
    min_deposit = db.Column(db.Integer)
    url = db.Column(db.String(255))
    is_featured = db.Column(db.Boolean, default=False)
    is_new = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f'<Casino {self.name}>'

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    casino_id = db.Column(db.Integer, db.ForeignKey('casino.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pros = db.Column(db.Text)
    cons = db.Column(db.Text)
    published_date = db.Column(db.DateTime, default=func.now())
    
    casino = db.relationship('Casino', backref=db.backref('reviews', lazy=True))
    
    def __repr__(self):
        return f'<Review {self.title}>'

class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
    published_date = db.Column(db.DateTime, default=func.now())
    
    def __repr__(self):
        return f'<Tip {self.title}>'

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    
    def __repr__(self):
        return f'<Contact {self.email}>'