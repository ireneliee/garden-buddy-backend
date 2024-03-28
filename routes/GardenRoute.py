from ..services.GardenService import GardenService
from flask import jsonify, request


def setup_garden_routes(app):

  @app.route('/garden/getGardenTypeById', methods=['GET'])
  def getGardenTypeById():
      garden_type_id = request.args.get('id')
      garden_type = GardenService.get_garden_type_by_id(garden_type_id)
      return jsonify(garden_type.serialize())
  
  @app.route('/garden/getGardenBuddyById', methods=['GET'])
  def getGardenBuddyById():
      garden_buddy_id = request.args.get('id')
      garden_buddy = GardenService.get_garden_buddy_by_id(garden_buddy_id)
      return jsonify(garden_buddy.serialize())
    
  @app.route('/garden/createGardenBuddy', methods=['POST'])
  def createGardenBuddy():
      user_id = request.args.get('user_id')
      garden_buddy = GardenService.create_garden_buddy(user_id)
      return jsonify(garden_buddy.serialize())
  
  @app.route('/garden/createGarden', methods=['POST'])
  def createGarden():
      garden_buddy_id = request.args.get('garden_buddy_id')
      garden_type_id = request.args.get('garden_type_id')
      garden = GardenService.create_garden(garden_buddy_id, garden_type_id)
      return jsonify(garden.serialize())