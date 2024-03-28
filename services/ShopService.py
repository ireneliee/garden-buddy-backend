from ..models import db, GardenBuddyPack, Accessory

from datetime import datetime

class ShopService:
    @staticmethod
    def create_garden_buddy_pack(name, price, quantity, description, plant_name, garden_buddy_pack_description, environment_enum, garden_type_id):
        try:
            new_item = GardenBuddyPack(name=name, price=price, quantity=quantity, description=description,
                                       plant_name=plant_name, garden_buddy_pack_description=garden_buddy_pack_description,
                                       environment_enum=environment_enum, garden_type_id=garden_type_id)
            db.session.add(new_item)
            db.session.commit()
            return new_item.serialize()
        except Exception as e:
            db.session.rollback()
            return str(e)

    @staticmethod
    def get_garden_buddy_pack(item_id):
        item = GardenBuddyPack.query.get(item_id)
        if item:
            return item.serialize()
        return None

    @staticmethod
    def update_garden_buddy_pack(item_id, name=None, price=None, quantity=None, description=None,
                                 plant_name=None, garden_buddy_pack_description=None, environment_enum=None, garden_type_id=None):
        item = GardenBuddyPack.query.get(item_id)
        if item:
            if name:
                item.name = name
            if price:
                item.price = price
            if quantity:
                item.quantity = quantity
            if description:
                item.description = description
            if plant_name:
                item.plant_name = plant_name
            if garden_buddy_pack_description:
                item.garden_buddy_pack_description = garden_buddy_pack_description
            if environment_enum:
                item.environment_enum = environment_enum
            if garden_type_id:
                item.garden_type_id = garden_type_id

            db.session.commit()
            return item.serialize()
        return None

    @staticmethod
    def delete_garden_buddy_pack(item_id):
        item = GardenBuddyPack.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return item.serialize()
        return None

    @staticmethod
    def create_accessory(name, price, quantity, description):
        try:
            new_item = Accessory(name=name, price=price, quantity=quantity, description=description)
            db.session.add(new_item)
            db.session.commit()
            return new_item.serialize()
        except Exception as e:
            db.session.rollback()
            return str(e)

    @staticmethod
    def get_accessory(item_id):
        item = Accessory.query.get(item_id)
        if item:
            return item.serialize()
        return None

    @staticmethod
    def update_accessory(item_id, name=None, price=None, quantity=None, description=None):
        item = Accessory.query.get(item_id)
        if item:
            if name:
                item.name = name
            if price:
                item.price = price
            if quantity:
                item.quantity = quantity
            if description:
                item.description = description

            db.session.commit()
            return item.serialize()
        return None

    @staticmethod
    def delete_accessory(item_id):
        item = Accessory.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return item.serialize()
        return None
