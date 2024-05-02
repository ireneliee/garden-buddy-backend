from ..services.DataService import DataService

from flask import jsonify, request


def setup_data_routes(app):
  @app.route('/data/submitTemperatureData', methods=['POST'])
  def submitTemperatureData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeTemperatureData(serial_id = identifier, air_temperature = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitMoistureData', methods=['POST'])
  def submitMoistureData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeMoistureData(serial_id = identifier, moisture = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitSalinityData', methods=['POST'])
  def submitSalinityData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeSalinityData(serial_id= identifier, salinity = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitPhData', methods=['POST'])
  def submitPhData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storePhData(serial_id = identifier, ph = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitBrightnessData', methods=['POST'])
  def submitBrightnessData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeBrightnessData(serial_id = identifier, brightness = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitHeightData', methods=['POST'])
  def submitHeightData():
      identifier = request.form.get('identifier')
      value = request.form.get('value')
      garden_data = DataService.storeHeightData(serial_id = identifier, height = value)
      return jsonify(garden_data.serialize())
  
  @app.route('/data/submitPictureData', methods=['POST'])
  def submitPictureData():
    identifier = request.form.get('identifier')
    file = request.files.get('file')
    garden_data = DataService.storePictureData(serial_id=identifier, file=file)
    return jsonify(garden_data.serialize())
  
  @app.route('/data/getGardenTypeBySerialId', methods=['GET'])
  def getGardenTypeBySerialId():
      serial_id = request.args.get('serialId')
      ideal_features = DataService.get_garden_type_by_serial(serial_id)
      return jsonify(ideal_features)
  
  
  @app.route('/data/testing', methods=['GET'])
  def testing():
      print('Called')
      return "testing"
