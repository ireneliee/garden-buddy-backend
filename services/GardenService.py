from ..models import db, GardenType,GardenBuddy, Garden, User
from datetime import datetime
import bcrypt
from sqlalchemy.exc import IntegrityError
from flask import current_app
from .UserService import UserService


class GardenService:

    @staticmethod
    def get_garden_type_by_id(id):
      garden_type = GardenType.query.get(id)
      if not garden_type:
        raise ValueError("garden_type not found")
      return garden_type
    
    @staticmethod
    def get_garden_buddy_by_id(id):
      garden_buddy = GardenBuddy.query.get(id)
      if not garden_buddy:
        raise ValueError("garden_buddy not found")
      return garden_buddy
    
    @staticmethod
    def create_garden_type(plant_name, plant_description, ideal_ph_level, ideal_temp_level, ideal_moisture_level, ideal_soil_salinity, ideal_light):
      garden_type = GardenType(plant_name=plant_name, plant_description=plant_description, ideal_ph_level=ideal_ph_level, ideal_temp_level=ideal_temp_level, ideal_moisture_level=ideal_moisture_level, ideal_soil_salinity=ideal_soil_salinity, ideal_light = ideal_light)
      db.session.add(garden_type)
      db.session.commit()        
      return  garden_type
    
    @staticmethod  
    def create_garden_buddy(user_id, serial_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            date_registered = datetime.now()
            garden_buddy = GardenBuddy(date_registered=date_registered,serial_id=str(serial_id), user_id=user_id, user=user)
            db.session.add(garden_buddy)
            db.session.commit()
            return garden_buddy
        else:
            raise ValueError("User not found")
        
    @staticmethod
    def create_garden(garden_buddy_id, garden_type_id):
        garden_type = GardenService.get_garden_type_by_id(garden_type_id)
        garden_buddy = GardenService.get_garden_buddy_by_id(garden_buddy_id)

        garden = Garden(garden_type_id=garden_type_id, garden_type=garden_type )
        garden_buddy.garden = garden
        db.session.add(garden)
        db.session.commit()       

        return garden
    
    @staticmethod
    def get_garden_buddies_by_user_id(user_id):
      user = UserService.get_user_by_id(user_id)
      print(user)
      garden_buddies = user.garden_buddies

      print(user.garden_buddies)
      return garden_buddies
    
    @staticmethod
    def get_garden_by_garden_buddy_id(garden_buddy_id):
      garden_buddy = GardenBuddy.query.get(garden_buddy_id)
      return garden_buddy.garden

    @staticmethod
    def get_all_garden_types():
      return GardenType.query.all()