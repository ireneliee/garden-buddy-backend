import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import joblib

class HealthPredictionService:
    
    @staticmethod
    def detect_harmful_patterns(image_path):
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros_like(img)
        cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
        result = cv2.addWeighted(img, 1, mask, 0.5, 0)
        
        image_filename = os.path.basename(image_path)
        output_filename = image_filename.replace(".jpg", "_highlighted.jpg")
        output_directory = os.path.join("static/highlighted_patterns", output_filename)
        
        cv2.imwrite(output_directory, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
        return output_directory
    
    @staticmethod
    def get_predicted_label(image_path):
        model = joblib.load('services/health_prediction_model.joblib')
        image = cv2.imread(image_path)
        image = cv2.resize(image, (256, 256))
        image = np.expand_dims(image, axis=0) / 255.0
        prediction = model.predict(image)
        predicted_label_index = np.argmax(prediction)
        label_map = {0: 'healthy', 1: 'multiple_diseases', 2: 'rust', 3: 'scab'}
        predicted_label = label_map.get(predicted_label_index, 'unknown')
        return predicted_label