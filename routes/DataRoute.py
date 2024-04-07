from ..services.DataService import DataService

from flask import jsonify, request


def setup_data_routes(app):

  @app.route('/data/submitTemperatureData', methods=['POST'])
  def submitTemperatureData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeTemperatureData(rpi_identifier = identifier, air_temperature = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitMoistureData', methods=['POST'])
  def submitMoistureData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeMoistureData(rpi_identifier = identifier, moisture = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitSalinityData', methods=['POST'])
  def submitSalinityData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeSalinityData(rpi_identifier = identifier, salinity = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitPhData', methods=['POST'])
  def submitPhData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storePhData(rpi_identifier = identifier, ph = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/testing', methods=['GET'])
  def testing():
      print('Called')
      return "testing"