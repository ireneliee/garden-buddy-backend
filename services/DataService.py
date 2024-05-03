from ..models import db, GardenBuddy, TemperatureData, BrightnessData, MoistureData, HeightData, SalinityData, PhData
from datetime import datetime
class DataService:
    
    @staticmethod
    def storeTemperatureData(serial_id, air_temperature):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id = serial_id).first()
            if garden_buddy:
                gardenData = TemperatureData(garden_id = garden_buddy.id, air_temperature = air_temperature, date_timestamp = date_timestamp )
                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError("Unable to find garden buddy associated with the serial id")
        
        except Exception as ex:
            print("An error occurred while storing temperature data:", ex)
            return None
    
    @staticmethod
    def storeMoistureData(serial_id, moisture):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id = serial_id).first()
            if garden_buddy:
                gardenData = MoistureData(garden_id = garden_buddy.id,moisture = moisture, date_timestamp = date_timestamp )
            
                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError("Unable to find garden_buddy associated with the serial_id")
        except Exception as ex:
            print("An error occurred while storing moisture data:", ex)
            return None
    
    @staticmethod
    def storeSalinityData(serial_id, salinity):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id = serial_id).first()
            if garden_buddy:

                gardenData = SalinityData(garden_id = garden_buddy.id, salinity = salinity, date_timestamp = date_timestamp )
            
                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError("Unable to find garden_buddy associated with the serial_id")
        
        except Exception as ex:
            print("An error occurred while storing salinity data:", ex)
            return None
        
    @staticmethod
    def storePhData(serial_id, ph):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id = serial_id).first()
            if garden_buddy:
                gardenData = PhData(garden_id = garden_buddy.id, ph = ph, date_timestamp = date_timestamp )
            
                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError("Unable to find garden_buddy associated with the serial_id")
        
        except Exception as ex:
            print("An error occurred while storing ph data:", ex)
            return None

    @staticmethod
    def storeBrightnessData(serial_id, brightness):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id = serial_id).first()
            if garden_buddy:
                gardenData = BrightnessData(garden_id = garden_buddy.id, brightness = brightness, date_timestamp = date_timestamp )
            
                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError("Unable to find garden_buddy associated with the serial_id")
        except Exception as ex:
            print("An error occurred while storing ph data:", ex)
            return None
    
    @staticmethod
    def storeHeightData(serial_id, height):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id = serial_id).first()
            if garden_buddy:
                gardenData = HeightData(garden_id = garden_buddy.id, height = height, date_timestamp = date_timestamp )
            
                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError("Unable to find garden_buddy associated with the serial_id")
        
        except Exception as ex:
            print("An error occurred while storing ph data:", ex)
            return None
    
    #AMELIA HERE
    @staticmethod
    def get_phdata_by_garden_id(garden_id):
        try:
            ph_data = PhData.query.filter_by(garden_id=garden_id)\
                               .order_by(PhData.date_timestamp.desc()).first()
            if ph_data:
                return ph_data.ph
            else:
                return 'No pH data found for this garden type.'
        except Exception as e:
            return f"An error occurred: {e}"

    
