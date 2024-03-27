from ..models import db, User
from datetime import datetime

class UserService:

    @staticmethod
    def create_user(username, password, firstname, lastname):
        try:
            user_start_date = datetime.now()
            user = User(username=username, password=password, firstname=firstname, lastname=lastname, user_start_date=user_start_date)
            db.session.add(user)
            db.session.commit()
            return user
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