from ..services.UserService import UserService
from flask import jsonify

def setup_user_routes(app):
  @app.route('/user/getAllUsers')
  def getAllUsers():
      users = UserService.get_all_users()
      return jsonify([user.serialize() for user in users])
