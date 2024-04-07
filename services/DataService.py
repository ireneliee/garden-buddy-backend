from ..models import db, GardenTemperatureData, GardenMoistureData, GardenSalinityData, GardenPhData
from datetime import datetime
class DataService:

    @staticmethod
    def storeTemperatureData(rpi_identifier, air_temperature):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            gardenData = GardenTemperatureData(rpi_identifier = rpi_identifier, air_temperature = air_temperature, date_timestamp = date_timestamp )
            db.session.add(gardenData)
            db.session.commit()
            return gardenData
        
        except Exception as ex:
            print("An error occurred while storing temperature data:", ex)
            return None
    
    @staticmethod
    def storeMoistureData(rpi_identifier, moisture):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            gardenData = GardenMoistureData(rpi_identifier = rpi_identifier,moisture = moisture, date_timestamp = date_timestamp )
          
            db.session.add(gardenData)
            db.session.commit()
            return gardenData
        
        except Exception as ex:
            print("An error occurred while storing moisture data:", ex)
            return None
    
    @staticmethod
    def storeSalinityData(rpi_identifier, salinity):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            gardenData = GardenSalinityData(rpi_identifier = rpi_identifier,salinity = salinity, date_timestamp = date_timestamp )
          
            db.session.add(gardenData)
            db.session.commit()
            return gardenData
        
        except Exception as ex:
            print("An error occurred while storing salinity data:", ex)
            return None
        
    @staticmethod
    def storePhData(rpi_identifier, ph):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            gardenData = GardenPhData(rpi_identifier = rpi_identifier, ph = ph, date_timestamp = date_timestamp )
          
            db.session.add(gardenData)
            db.session.commit()
            return gardenData
        
        except Exception as ex:
            print("An error occurred while storing ph data:", ex)
            return None
        
