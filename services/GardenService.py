from ..models import db, GardenType
from datetime import datetime
import bcrypt
from sqlalchemy.exc import IntegrityError
from flask import current_app


class GardenService:

    @staticmethod
    def create_garden_type(plant_name, plant_description, ideal_ph_level, ideal_temp_level, ideal_moisture_level, ideal_soil_salinity):
            gardenType = GardenType(plant_name=plant_name, plant_description=plant_description, ideal_ph_level=ideal_ph_level, ideal_temp_level=ideal_temp_level, ideal_moisture_level=ideal_moisture_level, ideal_soil_salinity=ideal_soil_salinity)
            db.session.add(gardenType)
            db.session.commit()        
            return  gardenType