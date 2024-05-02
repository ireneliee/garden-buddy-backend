from ..models import db, GardenType, GardenBuddy, Garden, User

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

class HeightPredictionModel:
    
    @staticmethod
    def train_logistic_regression():
        gardens = Garden.query.all()
        X = []
        y = []
        for garden in gardens:
            X.append([garden.ph_data.ph, garden.temperature_data.air_temperature, garden.salinity_data.salinity, garden.moisture_data.moisture])
            y.append(garden.height_data.height)
            
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        log_reg_model = LogisticRegression()
        log_reg_model.fit(X_train, y_train)
        
        joblib.dump(log_reg_model, 'services/logistic_regression_model.joblib')
        
        return X_train, X_test, y_train, y_test
    
    @staticmethod
    def train_svm():
        gardens = Garden.query.all()
        X = []
        y = []
        for garden in gardens:
            X.append([garden.ph_data.ph, garden.temperature_data.air_temperature, garden.salinity_data.salinity, garden.moisture_data.moisture])
            y.append(garden.height_data.height)
            
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        svm_model = SVC()
        svm_model.fit(X_train, y_train)
        
        joblib.dump(svm_model, 'services/svm_model.joblib')
        
        return X_train, X_test, y_train, y_test