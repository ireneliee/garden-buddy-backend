from ..services.UserService import UserService
from ..services.ShopService import ShopService
from ..services.GardenService import GardenService

from flask import jsonify, request


def setup_shop_routes(app):

  @app.route('/shop/createOrder', methods=['POST'])
  def createOrder():
      data = request.json 
      list_of_line_items = data.get('list_of_line_items')
      user_id = data.get('user_id')
      order = ShopService.create_order(list_of_line_items, user_id)
      return jsonify(order.serialize())
  

  @app.route('/shop/getAllAccessories', methods=['GET'])
  def getAllAccessories():
      accessories = ShopService.get_all_accessories()
      return jsonify([acc.serialize() for acc in accessories])
  
  @app.route('/shop/getAllGardenBuddyPacks', methods=['GET'])
  def getAllGardenBuddyPacks():
      packs = ShopService.get_all_garden_buddy_packs()
      return jsonify([pack.serialize() for pack in packs])
  
  @app.route('/shop/getInventoryItem', methods=['GET'])
  def getInventoryItem():
      item_id = request.args.get('item_id')
      item = ShopService.get_inventory_item(item_id)
      return jsonify(item.serialize())