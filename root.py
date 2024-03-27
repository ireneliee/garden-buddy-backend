# from flask import Flask, render_template
# from .config import Config
# from .services import user_service
# from . import db

# app = Flask(__name__, static_url_path='/static')
# app.config.from_object(Config)

# db.init_app(app)

# @app.route('/')
# def index():
#     return render_template('index.html', title="Garden Buddy Homepage", content="I love Garden Buddy")



# if __name__ == '__main__':

#     def create_sample_users():
#         print("Creating sample users")
#         users = [
#             {'username': 'user1', 'password': 'password1', 'firstname': 'John', 'lastname': 'Doe', 'user_start_date': '2022-01-01'},
#             {'username': 'user2', 'password': 'password2', 'firstname': 'Jane', 'lastname': 'Smith', 'user_start_date': '2022-01-01'}
#             # Add more sample users as needed
#         ]
#         for user_data in users:
#             user = user_service.create_user(**user_data)
#             print(f"Created user: {user}")
#         print("Finished creating sample users")
#         print("STARTED")

#     with app.app_context():
#         print("CALLING")
#         db.create_all() 
#         create_sample_users()
#     app.run(debug=False)
    
#     print("PASSED")

# print("PASSED 2")

# db.create_all() 

# users = [
#     {'username': 'user12', 'password': 'password12', 'firstname': 'John', 'lastname': 'Doe', 'user_start_date': '2022-01-01'},
#     {'username': 'user22', 'password': 'password22', 'firstname': 'Jane', 'lastname': 'Smith', 'user_start_date': '2022-01-01'}
#     # Add more sample users as needed
# ]
# for user_data in users:
#     user = user_service.create_user(**user_data)
#     print(f"Created user: {user}")

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:password@localhost/garden_buddy_database'
# initialize the app with the extension
db.init_app(app)


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


class GardenBuddy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_registered = db.Column(db.DateTime, nullable=False)  

    # Define user_id as a foreign key for the relationship with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define the back reference for the relationship
    user = relationship('User', back_populates='garden_buddies')

    def __repr__(self):
        return f'<GardenBuddy {self.id}>'
    

class UserService:
    # def __init__(self, db):
    #     self.db = db

  @staticmethod
  def create_user(username, password, firstname, lastname, user_start_date):
      print("CALLIING CREATE")
      user = User(username=username, password=password, firstname=firstname, lastname=lastname, user_start_date=user_start_date)
      db.session.add(user)
      db.session.commit()
      return user

  @staticmethod
  def get_user_by_id(user_id):
      return User.query.get(user_id)

  @staticmethod
  def update_user(user_id, username=None, password=None, firstname=None, lastname=None, user_start_date=None):
      user = User.query.get(user_id)
      if user:
          if username:
              user.username = username
          if password:
              user.password = password
          if firstname:
              user.firstname = firstname
          if lastname:
              user.lastname = lastname
          if user_start_date:
              user.user_start_date = user_start_date
          db.session.commit()
      return user

  @staticmethod
  def delete_user(user_id):
      user = User.query.get(user_id)
      if user:
          db.session.delete(user)
          db.session.commit()

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
    print("Finished creating sample users")

    # with app.app_context():
    #     print("CALLING")
    #     db.create_all() 
    #     create_sample_users()
    # app.run(debug=False)
    
# with app.app_context():
#     db.create_all()
    
@app.route('/')
def index():
    return render_template('index.html', title="Garden Buddy Homepage", content="I love Garden Buddy")


with app.app_context():
    print("CALLING")
    db.create_all() 
    create_sample_users()
app.run(debug=False)