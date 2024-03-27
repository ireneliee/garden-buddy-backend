# from flask import Flask
# from .config import Config
# from .models import db, User
# from .services.UserService import UserService
# from .routes import AppRoute, UserRoute
# import connexion


# from sqlalchemy import inspect

# # app = Flask(__name__, static_url_path='/static')
# app = connexion.App(__name__, specification_dir='./')
# app.add_api('openapi/swagger.yml')

# app.config.from_object(Config)
# db.init_app(app)

# # dataloader method (consider refactoring)
# def create_sample_users():
#     print("Creating sample users")
#     users = [
#         {'username': 'user1', 'password': 'password1', 'firstname': 'John', 'lastname': 'Doe', 'user_start_date': '2022-01-01'},
#         {'username': 'user2', 'password': 'password2', 'firstname': 'Jane', 'lastname': 'Smith', 'user_start_date': '2022-01-01'}
#     ]
#     for user_data in users:
#         user = UserService.create_user(**user_data)
#         print(f"Created user: {user}")

# # dataloader and init db
# with app.app_context():
#     inspector = inspect(db.engine)
#     if not inspector.has_table(User.__tablename__):
#         db.create_all()
#         create_sample_users()

# # load in routes
# AppRoute.setup_app_routes(app)
# UserRoute.setup_user_routes(app)

# # run app
# if __name__ == '__main__':
#     # app.run(debug=False)
#     app.run(host='0.0.0.0', port=5000)


from .config import Config
from .models import db, User
from .services.UserService import UserService
from .routes import AppRoute, UserRoute
import connexion

from sqlalchemy import inspect

# Load configuration
config = Config()

# Initialize connexion app
app = connexion.App(__name__, specification_dir='./')

# Add the API specification
app.add_api('openapi/swagger.yml')
# app.add_api('swagger.yml')

# Configure Flask app using Connexion's underlying Flask app
flask_app = app.app
flask_app.config.from_object(config)

# Initialize database
db.init_app(flask_app)

# dataloader method (consider refactoring)
def create_sample_users():
    print("Creating sample users")
    users = [
        {'username': 'user1', 'password': 'password1', 'firstname': 'John', 'lastname': 'Doe'},
        {'username': 'user2', 'password': 'password2', 'firstname': 'Jane', 'lastname': 'Smith'}
    ]
    for user_data in users:
        user = UserService.create_user(**user_data)
        print(f"Created user: {user}")

# dataloader and init db
with flask_app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table(User.__tablename__):
        db.create_all()
        create_sample_users()

# load in routes
AppRoute.setup_app_routes(flask_app)
UserRoute.setup_user_routes(flask_app)

# run app
if __name__ == '__main__':
    app.run(port=5000)
