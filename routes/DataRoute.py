from ..services.UserService import UserService
from ..services.ShopService import ShopService
from ..services.GardenService import GardenService
from ..services.DataService import DataService

from flask import jsonify, request


def setup_data_routes(app):

  @app.route('/data/xxx', methods=['POST'])
  def xxx():
    pass