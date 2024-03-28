from ..models import db, User
from datetime import datetime
import bcrypt
from sqlalchemy.exc import IntegrityError
from flask import current_app


class UserService:

    @staticmethod
    def hash_password(password):
        secret_key = current_app.config['SECRET_KEY']
        return  bcrypt.hashpw((password + secret_key).encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def create_user(username, password, firstname, lastname):
        try:
            existing_user = UserService.get_user_by_username(username)
            if existing_user:
                raise ValueError("Username already exists")
        
            hashed_password = UserService.hash_password(password)
            user_start_date = datetime.now()
            user = User(username=username, password=hashed_password.decode("utf-8"), firstname=firstname, lastname=lastname, user_start_date=user_start_date)
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Username already exists")
        except Exception as ex:
            print("An error occurred while creating the user:", ex)
            return None
        
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_user(user_id, username=None, password=None, firstname=None, lastname=None):
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
            db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            if len(user.garden_buddies) == 0 and len(user.orders) == 0:
                db.session.delete(user)
                db.session.commit()
                return {'message': 'User deleted successfully'}
            else:
                return {'message': 'User has associated garden buddies or orders and cannot be deleted'}
        else:
            return {'message': 'User not found'}
        
    @staticmethod
    def user_login(username, password):
        user = UserService.get_user_by_username(username)
        if user:
            secret_key = current_app.config['SECRET_KEY']
            if bcrypt.checkpw((password + secret_key).encode('utf-8'), user.password.encode("utf-8")):
                return {'message': 'Login successful', 'user_id': user.id}
        
        return {'message': 'Login failed'}