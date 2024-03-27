from flask import Flask
from .config import Config
from .models import db, User
from .services.UserService import UserService
from .routes import AppRoute, UserRoute

from sqlalchemy import inspect

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
db.init_app(app)

# dataloader method (consider refactoring)
def create_sample_users():
    print("Creating sample users")
    users = [
        {'username': 'user1', 'password': 'password1', 'firstname': 'John', 'lastname': 'Doe', 'user_start_date': '2022-01-01'},
        {'username': 'user2', 'password': 'password2', 'firstname': 'Jane', 'lastname': 'Smith', 'user_start_date': '2022-01-01'}
    ]
    for user_data in users:
        user = UserService.create_user(**user_data)
        print(f"Created user: {user}")

# dataloader and init db
with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table(User.__tablename__):
        db.create_all()
        create_sample_users()

# load in routes
AppRoute.setup_app_routes(app)
UserRoute.setup_user_routes(app)

# run app
if __name__ == '__main__':
    app.run(debug=False)
