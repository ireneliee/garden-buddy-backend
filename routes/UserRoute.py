from ..services.UserService import UserService
from flask import jsonify, request


def setup_user_routes(app):
  @app.route('/users/createUser', methods=['POST'])
  def createUser():
      username = request.args.get('username')
      password = request.args.get('password')
      firstname = request.args.get('firstname')
      lastname = request.args.get('lastname')
      user = UserService.create_user(username, password, firstname, lastname)
      return jsonify(user.serialize())
  
  @app.route('/users/userLogin', methods=['POST'])
  def userLogin():
      username = request.args.get('username')
      password = request.args.get('password')
      user = UserService.user_login(username, password)
      return jsonify(user)

  @app.route('/users/getAllUsers', methods=['GET'])
  def getAllUsers():
      users = UserService.get_all_users()
      return jsonify([user.serialize() for user in users])
  
  @app.route('/users/getUserById', methods=['GET'])
  def getUserById():
      userId = request.args.get('userId')
      user = UserService.get_user_by_id(userId)
      return jsonify(user.serialize())
  
  @app.route('/users/getOrdersByUserId', methods=['GET'])
  def getOrdersByUserId():
      userId = request.args.get('userId')
      orders = UserService.get_orders_by_userId(userId)
      return jsonify([order.serialize() for order in orders])
  
  @app.route('/users/getOrdersByOrderId', methods=['GET'])
  def getOrdersByOrderId():
      orderId = request.args.get('orderId')
      orders = UserService.get_orders_by_orderId(orderId)
      return jsonify([order.serialize() for order in orders])
  
#DO NOT USE UPDATE OR DELETE
  @app.route('/users/updateUser', methods=['PUT'])
  def updateUser():
      userId = request.args.get('userId')
      username = request.args.get('username')
      password = request.args.get('password')
      firstname = request.args.get('firstname')
      lastname = request.args.get('lastname')
      user = UserService.update_user(userId,username,password,firstname,lastname)
      return jsonify(user.serialize())

  @app.route('/users/deleteUser', methods=['DELETE'])
  def deleteUser():
      userId = request.args.get('userId')
      UserService.delete_user(userId)
      return jsonify({'message': 'User deleted successfully'})