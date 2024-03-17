from app import db

class Property(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    bedrooms = db.Column(db.String(50), nullable=False)
    bathrooms = db.Column(db.String(50), nullable=False)
    
    price = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    
    location = db.Column(db.String(255), nullable=False)

    photo = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f"Property('{self.title}', '{self.location}', '{self.price}')"