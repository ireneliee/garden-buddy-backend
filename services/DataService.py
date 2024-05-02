from ..models import db, Garden, GardenType, GardenBuddy, TemperatureData, BrightnessData, MoistureData, HeightData, SalinityData, PhData
from datetime import datetime
from flask import current_app

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
    def get_garden_type_by_serial(serialNumber):
       
       garden_buddy = GardenBuddy.query.filter_by(serial_id = serialNumber).first() 
       if not garden_buddy:
          raise ValueError("Garden buddy not found")
       
       garden_type = GardenType.query.get(garden_buddy.garden.garden_type_id)

       if not garden_type:
          raise ValueError("Garden type doesn't exist")
       
       return garden_type
    
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
        
    @staticmethod
    def retrieveLatestData(gardenId):
        try:
            data_pack = {}

            latest_temperature_data = TemperatureData.query.filter_by(garden_id = gardenId).order_by(TemperatureData.date_timestamp.desc()).first()
            data_pack['temperature'] = latest_temperature_data

            latest_brightness_data = BrightnessData.query.filter_by(garden_id = gardenId).order_by(BrightnessData.date_timestamp.desc()).first()
            data_pack['brightness'] = latest_brightness_data

            latest_salinity_data = SalinityData.query.filter_by(garden_id = gardenId).order_by(SalinityData.date_timestamp.desc()).first()
            data_pack['salinity'] = latest_salinity_data

            latest_ph_data = PhData.query.filter_by(garden_id = gardenId).order_by(PhData.date_timestamp.desc()).first()
            data_pack['ph'] = latest_ph_data

            latest_moisture_data = MoistureData.query.filter_by(garden_id = gardenId).order_by(MoistureData.date_timestamp.desc()).first()
            data_pack['moisture'] = latest_moisture_data

            return data_pack

        except Exception as ex:
            print("An error occurred while retrieving latest garden data: ", ex)
    
    @staticmethod
    def retrieveIdealCondition(gardenTypeId):
        ideal_data = GardenType.query.filter_by(id = gardenTypeId).first()
        print('Reach X')
        return ideal_data
    
    @staticmethod
    def retrieveAbnormalCondition(gardenId):
        print('Reach A')
        latest_data = DataService.retrieveLatestData(gardenId)
        print('Reach B')
        garden_object = Garden.query.filter_by(id = gardenId).first()
        print('Reach C')
        ideal_data = DataService.retrieveIdealCondition(garden_object.garden_type_id)
        print('Reach D')

        abnormal_data = {}
        print('Reach E')
        temperature_range = current_app.config['TEMPERATURE_RANGE']
        brightness_range = current_app.config['BRIGHTNESS_RANGE']
        salinity_range = current_app.config['SALINITY_RANGE']
        ph_range = current_app.config('PH_RANGE')
        moisture_range = current_app.config('BRIGHTNESS_RANGE')


        print('Reach F')


        if latest_data and ideal_data:
            if latest_data['temperature'] and ideal_data.ideal_temp_level:
                if not (ideal_data.ideal_temp_level - temperature_range <= latest_data['temperature'] <= ideal_data.ideal_temp_level + temperature_range):
                    abnormal_data['temperature'] = latest_data['temperature']
            
            if latest_data['brightness'] and ideal_data.ideal_light:
                if latest_data['brightness'] > ideal_data.ideal_light - brightness_range <= latest_data['brightness'] <= ideal_data.ideal_light + brightness_range:
                    abnormal_data['brightness'] = latest_data['brightness']
            
            if latest_data['salinity'] and ideal_data.ideal_soil_salinity:
                if latest_data['salinity'] > ideal_data.ideal_soil_salinity - salinity_range <= latest_data['salinity'] <= ideal_data.ideal_soil_salinity + salinity_range:
                    abnormal_data['salinity'] = latest_data['salinity']
            
            if latest_data['ph'] and ideal_data.ideal_ph_level:
                if latest_data['ph'] > ideal_data.ideal_ph_level - ph_range <= latest_data['ph'] <= ideal_data.ideal_ph_level + ph_range:
                    abnormal_data['ph'] = latest_data['ph']
            
            if latest_data['moisture'] and ideal_data.ideal_moisture_level:
                if latest_data['moisture'] > ideal_data.ideal_moisture_level - moisture_range <= latest_data['moisture'] <= ideal_data.ideal_moisture_level + moisture_range:
                    abnormal_data['moisture'] = latest_data['moisture']
    
        return abnormal_data



    
