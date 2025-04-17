from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask app and extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Initialize SQLAlchemy and LoginManager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Create a simple route for the home page
@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
