from app import db

class Property(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    
    location = db.Column(db.String(255), nullable=False)

    photo = db.Column(db.String(255), nullable=False)
    
    # Validation
    __table_args__ = (
        db.CheckConstraint('bedrooms >= 0'),
        db.CheckConstraint('bathrooms >= 0'),
    )

    def __repr__(self):
        return f"Property('{self.title}', '{self.location}', '{self.price}')"