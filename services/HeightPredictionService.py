from ..models import db, GardenData, GardenType, GardenBuddy, Garden, User
from datetime import datetime
import bcrypt
from sqlalchemy.exc import IntegrityError
from .UserService import UserService

import time
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

class HeightPredictionModel:
    
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
    
    # Adjust Ideal Temp / etc.. values? When is ideal temp used.