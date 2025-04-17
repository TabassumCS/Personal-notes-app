# Import SQLAlchemy to interact with the database
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

#define the User model class to represent users in the database
class User(db.Model):
    #Define the primary key column for the user
    id = db.Column(db.Integer, primary_key=True)
    
    #Define the username column (sould be unique and cannot be empty)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    #Define te password_hash column (cannot be empty)
    password_hash = db.Column(db.String(128), nullable=False)

