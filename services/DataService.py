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
)
from datetime import datetime
import os
from flask import url_for
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
    def storeMoistureData(serial_id, moisture):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                gardenData = MoistureData(
                    garden_id=garden_buddy.id,
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
                    garden_id=garden_buddy.id,
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
                    garden_id=garden_buddy.id, ph=ph, date_timestamp=date_timestamp
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
                    garden_id=garden_buddy.id,
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

    @staticmethod
    def storeHeightData(serial_id, height):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                gardenData = HeightData(
                    garden_id=garden_buddy.id,
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
    def storePictureData(serial_id, file):
        try:
            date_timestamp = datetime.now().replace(microsecond=0)
            garden_buddy = GardenBuddy.query.filter_by(serial_id=serial_id).first()
            if garden_buddy:
                file_name = f"{serial_id}.jpg"
                file_path = os.path.join("services/uploaded_pictures/", file_name)
                file.save(file_path)

                image_link = url_for(
                    "static", filename=f"uploaded_pictures/{file_name}", _external=True
                )

                garden_data = GardenImage(
                    garden_id=garden_buddy.garden.id,
                    image_link=image_link,
                    date_timestamp=date_timestamp,
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
