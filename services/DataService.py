from ..models import (
    db,
    GardenBuddy,
    TemperatureData,
    BrightnessData,
    MoistureData,
    HeightData,
    SalinityData,
    PhData,
    GardenImage,
    Garden,
    GardenType,
)
from datetime import datetime
import os
from flask import url_for, current_app

from sqlalchemy import desc


class DataService:

    @staticmethod
    def storeTemperatureData(serial_id, air_temperature):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                gardenData = TemperatureData(
                    garden_id=garden_buddy.id,
                    air_temperature=air_temperature,
                    date_timestamp=date_timestamp,
                )
                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError(
                    "Unable to find garden buddy associated with the serial id"
                )

        except Exception as ex:
            print("An error occurred while storing temperature data:", ex)
            return None

    @staticmethod
    def get_garden_type_by_serial(serialNumber):
        garden_buddy = GardenBuddy.query.filter_by(serial_id=serialNumber).first()

        if not garden_buddy:
            raise ValueError("Garden buddy not found")

        garden = Garden.query.get(garden_buddy.garden_id)

        gardenType = GardenType.query.get(garden.garden_type_id)

        gardenType = gardenType.serialize()
        return gardenType

    @staticmethod
    def storeMoistureData(serial_id, moisture):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                gardenData = MoistureData(
                    garden_id=garden_buddy.garden_id,
                    moisture=moisture,
                    date_timestamp=date_timestamp,
                )

                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError(
                    "Unable to find garden_buddy associated with the serial_id"
                )
        except Exception as ex:
            print("An error occurred while storing moisture data:", ex)
            return None

    @staticmethod
    def storeSalinityData(serial_id, salinity):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:

                gardenData = SalinityData(
                    garden_id=garden_buddy.garden_id,
                    salinity=salinity,
                    date_timestamp=date_timestamp,
                )

                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError(
                    "Unable to find garden_buddy associated with the serial_id"
                )

        except Exception as ex:
            print("An error occurred while storing salinity data:", ex)
            return None

    @staticmethod
    def storePhData(serial_id, ph):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                gardenData = PhData(
                    garden_id=garden_buddy.garden_id,
                    ph=ph,
                    date_timestamp=date_timestamp,
                )

                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError(
                    "Unable to find garden_buddy associated with the serial_id"
                )

        except Exception as ex:
            print("An error occurred while storing ph data:", ex)
            return None

    @staticmethod
    def storeBrightnessData(serial_id, brightness):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                gardenData = BrightnessData(
                    garden_id=garden_buddy.garden_id,
                    brightness=brightness,
                    date_timestamp=date_timestamp,
                )

                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError(
                    "Unable to find garden_buddy associated with the serial_id"
                )
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

    @staticmethod
    def storeHeightData(serial_id, height):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                gardenData = HeightData(
                    garden_id=garden_buddy.garden_id,
                    height=height,
                    date_timestamp=date_timestamp,
                )

                db.session.add(gardenData)
                db.session.commit()
                return gardenData
            else:
                raise ValueError(
                    "Unable to find garden_buddy associated with the serial_id"
                )

        except Exception as ex:
            print("An error occurred while storing ph data:", ex)
            return None
    
    @staticmethod
    def createHeightData(garden_id, height):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            gardenData = HeightData(
                    garden_id=garden_id,
                    height=height,
                    date_timestamp=date_timestamp,
                )
            db.session.add(gardenData)
            db.session.commit()
            return gardenData
        except Exception as ex:
            print("An error occurred while storing ph data:", ex)
            return None

    @staticmethod
    def retrieveLatestData(gardenId):
        try:
            data_pack = {}

            latest_temperature_data = (
                TemperatureData.query.filter_by(garden_id=gardenId)
                .order_by(TemperatureData.date_timestamp.desc())
                .first()
            )
            data_pack["temperature"] = latest_temperature_data

            latest_brightness_data = (
                BrightnessData.query.filter_by(garden_id=gardenId)
                .order_by(BrightnessData.date_timestamp.desc())
                .first()
            )
            data_pack["brightness"] = latest_brightness_data

            latest_salinity_data = (
                SalinityData.query.filter_by(garden_id=gardenId)
                .order_by(SalinityData.date_timestamp.desc())
                .first()
            )
            data_pack["salinity"] = latest_salinity_data

            latest_ph_data = (
                PhData.query.filter_by(garden_id=gardenId)
                .order_by(PhData.date_timestamp.desc())
                .first()
            )
            data_pack["ph"] = latest_ph_data

            latest_moisture_data = (
                MoistureData.query.filter_by(garden_id=gardenId)
                .order_by(MoistureData.date_timestamp.desc())
                .first()
            )
            data_pack["moisture"] = latest_moisture_data

            return data_pack

        except Exception as ex:
            print("An error occurred while retrieving latest garden data: ", ex)

    @staticmethod
    def retrieveIdealCondition(gardenTypeId):
        ideal_data = GardenType.query.filter_by(id=gardenTypeId).first()
        print("Reach X")
        return ideal_data

    @staticmethod
    def retrieveAbnormalCondition(gardenId):
        print("Reach A")
        latest_data = DataService.retrieveLatestData(gardenId)
        print("Reach B")
        garden_object = Garden.query.filter_by(id=gardenId).first()
        print("Reach C")
        ideal_data = DataService.retrieveIdealCondition(garden_object.garden_type_id)
        print("Reach D")

        abnormal_data = {}
        print("Reach E")
        temperature_range = current_app.config["TEMPERATURE_RANGE"]
        brightness_range = current_app.config["BRIGHTNESS_RANGE"]
        salinity_range = current_app.config["SALINITY_RANGE"]
        ph_range = current_app.config("PH_RANGE")
        moisture_range = current_app.config("BRIGHTNESS_RANGE")

        print("Reach F")

        if latest_data and ideal_data:
            if latest_data["temperature"] and ideal_data.ideal_temp_level:
                if not (
                    ideal_data.ideal_temp_level - temperature_range
                    <= latest_data["temperature"]
                    <= ideal_data.ideal_temp_level + temperature_range
                ):
                    abnormal_data["temperature"] = latest_data["temperature"]

            if latest_data["brightness"] and ideal_data.ideal_light:
                if (
                    latest_data["brightness"]
                    > ideal_data.ideal_light - brightness_range
                    <= latest_data["brightness"]
                    <= ideal_data.ideal_light + brightness_range
                ):
                    abnormal_data["brightness"] = latest_data["brightness"]

            if latest_data["salinity"] and ideal_data.ideal_soil_salinity:
                if (
                    latest_data["salinity"]
                    > ideal_data.ideal_soil_salinity - salinity_range
                    <= latest_data["salinity"]
                    <= ideal_data.ideal_soil_salinity + salinity_range
                ):
                    abnormal_data["salinity"] = latest_data["salinity"]

            if latest_data["ph"] and ideal_data.ideal_ph_level:
                if (
                    latest_data["ph"]
                    > ideal_data.ideal_ph_level - ph_range
                    <= latest_data["ph"]
                    <= ideal_data.ideal_ph_level + ph_range
                ):
                    abnormal_data["ph"] = latest_data["ph"]

            if latest_data["moisture"] and ideal_data.ideal_moisture_level:
                if (
                    latest_data["moisture"]
                    > ideal_data.ideal_moisture_level - moisture_range
                    <= latest_data["moisture"]
                    <= ideal_data.ideal_moisture_level + moisture_range
                ):
                    abnormal_data["moisture"] = latest_data["moisture"]

        return abnormal_data

    @staticmethod
    def storePictureData(serial_id, file):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                file_name = f"{serial_id}.jpg"
                file_path = os.path.join("services/uploaded_pictures/", file_name)
                file.save(file_path)

                image_link = "services/uploaded_pictures/" + file_name
                print('Image link is ', str(image_link))
                garden_data = GardenImage(
                    garden_id=garden_buddy.garden.id,
                    garden_image_link=image_link,
                    timestamp=date_timestamp,
                )
                db.session.add(garden_data)
                db.session.commit()
                return garden_data
            else:
                raise ValueError(
                    "Unable to find garden_buddy associated with the serial_id"
                )
        except Exception as ex:
            print("An error occurred while storing picture data:", ex)
            return None

    def getUserGardenData(garden_id):
        garden = Garden.query.get(garden_id)
        all_gardens = Garden.query.all()
        if not garden:
            print(garden_id)
            print(all_gardens)
            raise ValueError("garden not found")

        results = {}

        latest_moisture_data = (
            MoistureData.query.filter_by(garden_id=garden_id)
            .order_by(desc(MoistureData.date_timestamp))
            .first()
        )
        latest_temperature_data = (
            TemperatureData.query.filter_by(garden_id=garden_id)
            .order_by(desc(TemperatureData.date_timestamp))
            .first()
        )
        latest_ph_data = (
            PhData.query.filter_by(garden_id=garden_id)
            .order_by(desc(PhData.date_timestamp))
            .first()
        )
        latest_salinity_data = (
            SalinityData.query.filter_by(garden_id=garden_id)
            .order_by(desc(SalinityData.date_timestamp))
            .first()
        )
        latest_brightness_data = (
            BrightnessData.query.filter_by(garden_id=garden_id)
            .order_by(desc(BrightnessData.date_timestamp))
            .first()
        )
        latest_height_data = (
            HeightData.query.filter_by(garden_id=garden_id)
            .order_by(desc(HeightData.date_timestamp))
            .first()
        )

        if latest_height_data:
            results["curr_height"] = latest_height_data.height
        if latest_moisture_data:
            results["curr_moisture"] = latest_moisture_data.moisture
        if latest_temperature_data:
            results["curr_temperature"] = latest_temperature_data.air_temperature
        if latest_ph_data:
            results["curr_ph"] = latest_ph_data.ph
        if latest_salinity_data:
            results["curr_salinity"] = latest_salinity_data.salinity
        if latest_brightness_data:
            results["curr_brightness"] = latest_brightness_data.brightness

        # get garden ideal data
        results["ideal_moisture"] = garden.garden_type.ideal_moisture_level
        results["ideal_temperature"] = garden.garden_type.ideal_temp_level
        results["ideal_ph"] = garden.garden_type.ideal_ph_level
        results["ideal_salinity"] = garden.garden_type.ideal_soil_salinity
        # results["ideal_brightness"] = garden.garden_type.ideal_moisture_level

        return results
