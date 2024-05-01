from ..models import db, GardenData, GardenType, GardenBuddy, Garden, User

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

class HeightPredictionModel:
    
    @staticmethod
    def prepare_dataset():
        garden_data = GardenData.query.all()
        
        X = []
        y = []
        for data in garden_data:
            X.append([data.soil_ph_level, data.air_temperature, data.soil__salinity, data.soil_moisture])
            y.append(data.height_data.height)
        
        return X, y
    
    @staticmethod
    def train_logistic_regression(X_train, y_train):
        log_reg = LogisticRegression()
        log_reg.fit(X_train, y_train)
        return log_reg
    
    @staticmethod
    def train_svm(X_train, y_train):
        svm = SVC()
        svm.fit(X_train, y_train)
        return svm
    
    @staticmethod
    def save_model(model, filename):
        joblib.dump(model, filename)
        
X, y = HeightPredictionModel.prepare_dataset()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_reg_model = HeightPredictionModel.train_logistic_regression(X_train, y_train)
HeightPredictionModel.save_model(log_reg_model, 'logistic_regression_model.joblib')

svm_model = HeightPredictionModel.train_svm(X_train, y_train)
HeightPredictionModel.save_model(svm_model, 'svm_model.joblib')

# python3 -m services.HeightPredictionModel