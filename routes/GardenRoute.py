from ..services.GardenService import GardenService
from ..services.HeightPredictionModel import HeightPredictionModel
from ..services.HeightPredictionService import HeightPredictionService
from ..services.HealthPredictionModel import HealthPredictionModel
from ..services.HealthPredictionService import HealthPredictionService
from flask import jsonify, request
import numpy as np


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
      user_id = request.args.get('userId')
      serial_id = request.args.get('serialId')
      garden_buddy = GardenService.create_garden_buddy(user_id,serial_id)
      return jsonify(garden_buddy.serialize())
  
  @app.route('/garden/createGarden', methods=['POST'])
  def createGarden():
      garden_buddy_id = request.args.get('gardenBuddyId')
      garden_type_id = request.args.get('gardenTypeId')
      garden = GardenService.create_garden(garden_buddy_id, garden_type_id)
      return jsonify(garden.serialize())
  
  @app.route('/garden/getGardenBuddiesByUserId', methods=['GET'])
  def getGardenBuddiesByUserId():
      user_id = request.args.get('userId')
      print("received id: " + str(user_id))
      lst = GardenService.get_garden_buddies_by_user_id(user_id)
      print(lst)
      return jsonify([buddy.serialize() for buddy in lst])
  
  @app.route('/garden/getGardenByGardenBuddyId', methods=['GET'])
  def getGardenByGardenBuddyId():
      garden_buddy_id = request.args.get('gardenBuddyId')
      garden = GardenService.get_garden_by_garden_buddy_id(garden_buddy_id)
      if garden != None:
          return jsonify(garden.serialize())
      else:
          return {}
      
  @app.route('/garden/getAllGardenTypes', methods=['GET'])
  def getAllGardenTypes():
      garden_types = GardenService.get_all_garden_types()
      return jsonify([garden_type.serialize() for garden_type in garden_types])
  
  @app.route('/garden/height_prediction_model_train_logistic_regression', methods=['GET'])
  def trainLogisticRegression():
      HeightPredictionModel.train_logistic_regression()
      return {}
  
  @app.route('/garden/get_predicted_height_by_garden_id_logistic', methods=['GET'])
  def getPredictedHeightByGardenIdLogistic():
      garden_id = request.args.get('id')
      height = HeightPredictionService.get_predicted_height_by_id_logistic(garden_id)
      height_list = height.tolist() if isinstance(height, np.ndarray) else height
      return jsonify(height_list)
  
  @app.route('/garden/adjust_ideal_for_all_garden_type_logistic', methods=['GET'])
  def adjustIdealForAllGardenTypeLogistic():
      ideal_features = HeightPredictionService.adjust_ideal_for_all_garden_type_logistic()
      return jsonify(ideal_features)
  
  @app.route('/garden/height_prediction_model_train_svm', methods=['GET'])
  def trainSVM():
      HeightPredictionModel.train_svm()
      return {}
  
  @app.route('/garden/get_predicted_height_by_garden_id_svm', methods=['GET'])
  def getPredictedHeightByGardenIdSvm():
      garden_id = request.args.get('id')
      height = HeightPredictionService.get_predicted_height_by_id_svm(garden_id)
      height_list = height.tolist() if isinstance(height, np.ndarray) else height
      return jsonify(height_list)
  
  @app.route('/garden/adjust_ideal_for_all_garden_type_svm', methods=['GET'])
  def adjustIdealForAllGardenTypeSvm():
      ideal_features = HeightPredictionService.adjust_ideal_for_all_garden_type_svm()
      return jsonify(ideal_features)
  
  @app.route('/garden/health_prediction_model_train', methods=['GET'])
  def train():
      HealthPredictionModel.train()
      return {}
