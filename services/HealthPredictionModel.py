# Import necessary libraries
import os 
import cv2
import math
import random
import tensorflow as tf
import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from tqdm import tqdm
import plotly.express as px

from skimage import io, transform
from skimage.util import random_noise
from skimage import exposure
import skimage.io as skio

from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import imgaug as ia
from imgaug import augmenters as iaa

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential

class HealthPredictionModel:
    
    EPOCHS = 20
    SAMPLE_LEN = 100
    
    def __init__(self):
        self.model = self.train()
        self.image_directory = "services/cv_data/images/"
        self.output_directory = "services/cv_data/highlighted_patterns/"
    
    @staticmethod
    def load_image(image_id):
        file_path = os.path.join("services/cv_data/images/", image_id + ".jpg")
        image = cv2.imread(file_path)
        image = cv2.resize(image, (256, 256))
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def train():
        train_data = pd.read_csv('services/cv_data/train.csv')
        train_data = train_data.head(HealthPredictionModel.SAMPLE_LEN)

        train_images = []
        for image_id in tqdm(train_data["image_id"][:HealthPredictionModel.SAMPLE_LEN]):
            train_images.append(HealthPredictionModel.load_image(image_id))
        
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)))
        model.add(MaxPooling2D((2, 2)))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(4, activation='softmax'))
        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        
        train_labels = train_data[['healthy', 'multiple_diseases', 'rust', 'scab']].values
        print(train_labels)
        model.fit(np.array(train_images), train_labels, epochs=HealthPredictionModel.EPOCHS)
        
        joblib.dump(model, 'services/health_prediction_model.joblib')
        return model

# EPOCHS = 20
# SAMPLE_LEN = 100

# train_data = pd.read_csv('cv_data/train.csv')
# test_data = pd.read_csv("cv_data/test.csv")
# submission_data = pd.read_csv("cv_data/sample_submission.csv")
# image_directory = "cv_data/images/"
# image_files = os.listdir(image_directory)

# def load_image(image_id):
#     file_path = os.path.join(image_directory, image_id + ".jpg")
#     image = cv2.imread(file_path)
#     return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
# train_images = []
# for image_id in tqdm(train_data["image_id"][:SAMPLE_LEN]):
#     train_images.append(load_image(image_id))
    
# model = Sequential()
# model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)))
# model.add(MaxPooling2D((2, 2)))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D((2, 2)))
# model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(MaxPooling2D((2, 2)))
# model.add(Flatten())
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(4, activation='softmax'))
# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

# train_labels = train_data[['healthy', 'multiple_diseases', 'rust', 'scab']].values
# model.fit(np.array(train_images), train_labels, epochs=EPOCHS)

# test_image_ids = test_data['image_id'].tolist()
# test_images = []
# for image_id in test_image_ids:
#     image_path = os.path.join(image_directory, image_id + ".jpg")
#     image = cv2.imread(image_path)
#     image = cv2.resize(image, (256, 256))
#     test_images.append(image)

# test_images = np.array(test_images)
# test_images = test_images / 255.0

# predictions = model.predict(test_images) #label_map = {0: 'healthy', 1: 'multiple_diseases', 2: 'rust', 3: 'scab'}

# def detect_harmful_patterns_and_save(image_path):
#     img = cv2.imread(image_path)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     mask = np.zeros_like(img)
#     cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

#     result = cv2.addWeighted(img, 1, mask, 0.5, 0)
    
#     image_filename = os.path.basename(image_path)
    
#     output_filename = image_filename.replace(".jpg", "_highlighted.jpg")
#     output_directory = os.path.join("cv_data/highlighted_patterns", output_filename)
    
#     cv2.imwrite(output_directory, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))