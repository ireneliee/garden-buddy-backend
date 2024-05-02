from ..models import db, GardenData, GardenType, GardenBuddy, Garden, User
from datetime import datetime
import bcrypt
from sqlalchemy.exc import IntegrityError
from .UserService import UserService

import time
import numpy as np
import pandas as pd
import itertools
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

class HeightPredictionService:
    
    @staticmethod
    def get_predicted_height_by_id(id):
        garden = Garden.query.get(id)
        if not garden:
            raise ValueError("Garden not found")
        features = [garden.garden_data.soil_ph_level, garden.garden_data.air_temperature,
                    garden.garden_data.soil__salinity, garden.garden_data.soil_moisture]
        model = joblib.load('logistic_regression_model.joblib')
        predicted_height = model.predict([features])
        return predicted_height
    
    @staticmethod
    def adjust_ideal_for_all_garden_type(feature_names):
        feature_ranges = {
            'ideal_ph_level': (0, 14),
            'ideal_temp_level': (0, 100),
            'ideal_moisture_level': (0, 100),
            'ideal_soil_salinity': (0, 100)
        }
        feature_combinations = itertools.product(*(np.linspace(min_val, max_val, num=10) for min_val, max_val in feature_ranges.values()))
        
        max_predicted_height = -float('inf')
        ideal_features = None
        model = joblib.load('logistic_regression_model.joblib')
        for feature_values in feature_combinations:
            feature_dict = dict(zip(feature_names, feature_values))
            predicted_height = model.predict([list(feature_values)])
            if predicted_height > max_predicted_height:
                max_predicted_height = predicted_height
                ideal_features = feature_dict
                
        garden_types = GardenType.query.all()

        for garden_type in garden_types:
            garden_type.ideal_ph_level = ideal_features['ideal_ph_level']
            garden_type.ideal_temp_level = ideal_features['ideal_temp_level']
            garden_type.ideal_moisture_level = ideal_features['ideal_moisture_level']
            garden_type.ideal_soil_salinity = ideal_features['ideal_soil_salinity']

        db.session.commit()
        
        return ideal_features