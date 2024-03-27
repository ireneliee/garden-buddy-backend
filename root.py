from flask import Flask, render_template
from .config import Config
from .models import db, User, GardenBuddy
from .services.UserService import UserService
from sqlalchemy import inspect

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', title="Garden Buddy Homepage", content="I love Garden Buddy")

def create_sample_users():
    print("Creating sample users")
    users = [
        {'username': 'user1', 'password': 'password1', 'firstname': 'John', 'lastname': 'Doe', 'user_start_date': '2022-01-01'},
        {'username': 'user2', 'password': 'password2', 'firstname': 'Jane', 'lastname': 'Smith', 'user_start_date': '2022-01-01'}
        # Add more sample users as needed
    ]
    for user_data in users:
        user = UserService.create_user(**user_data)
        print(f"Created user: {user}")

with app.app_context():
    inspector = inspect(db.engine)
    # Check if User table exists
    if not inspector.has_table(User.__tablename__):
        db.create_all()
        create_sample_users()

if __name__ == '__main__':
    app.run(debug=False)
