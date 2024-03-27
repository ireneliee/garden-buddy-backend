from ..models import db, User

class UserService:

  @staticmethod
  def create_user(username, password, firstname, lastname, user_start_date):
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
