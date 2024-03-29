from ..services.UserService import UserService
from ..services.ShopService import ShopService
from ..services.GardenService import GardenService

from flask import jsonify, request


def setup_shop_routes(app):

  @app.route('/shop/createOrder', methods=['POST'])
  def createOrder():
      data = request.json  # This assumes the request's Content-Type is 'application/json'
      list_of_line_items = data.get('list_of_line_items')
      user_id = data.get('user_id')

      order = ShopService.create_order(list_of_line_items, user_id)
      return jsonify(order.serialize())