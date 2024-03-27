from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False) 
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    user_start_date = db.Column(db.DateTime, nullable=False) 

    # One-to-many relationship with GardenBuddy
    garden_buddies = relationship('GardenBuddy', back_populates='user')

    def __repr__(self):
        return f'<User {self.firstname} {self.lastname} {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'user_start_date': self.user_start_date.strftime('%Y-%m-%d')  # Convert to string
            # Add more fields if needed
        }


class GardenBuddy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_registered = db.Column(db.DateTime, nullable=False)  

    # Define user_id as a foreign key for the relationship with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define the back reference for the relationship
    user = relationship('User', back_populates='garden_buddies')

    def __repr__(self):
        return f'<GardenBuddy {self.id}>'
