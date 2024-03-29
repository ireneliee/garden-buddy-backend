from ..models import db, GardenBuddyPack, Accessory, Order, OrderLineItem, OrderStatus, InventoryItem
from.UserService import UserService
from datetime import datetime
from sqlalchemy.exc import IntegrityError

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

    @staticmethod
    def create_order_line_item(inventory_item_id, quantity):
        
        buddy_pack = ShopService.get_garden_buddy_pack(inventory_item_id)
        accessory = ShopService.get_accessory(inventory_item_id)

        item = None
        if buddy_pack != None:
            item = buddy_pack
        elif accessory != None:
            item = accessory
        else:
            raise ValueError("ITEM DOES NOT EXIST")
        
        inventory_item = ShopService.get_inventory_item(inventory_item_id)

        if inventory_item.quantity < quantity:
            raise ValueError("Not enough quantity for Inventory Item!")


        sub_total = inventory_item.price * quantity
        order_line_item = OrderLineItem(quantity=quantity,sub_total=sub_total, inventory_item_id=inventory_item_id)
        inventory_item.quantity = inventory_item.quantity - quantity

        db.session.add(order_line_item)
        db.session.commit()

        return order_line_item

    @staticmethod
    def create_order(list_of_line_items, user_id):
        try:
            user = UserService.get_user_by_id(user_id)
            lst = []
            total_price = 0
            for item in list_of_line_items:
                inventory_id = item[0]
                quantity = item[1] 
                order_line_item = ShopService.create_order_line_item(inventory_id,quantity)
                lst.append(order_line_item)
                total_price += order_line_item.sub_total

            order = Order(total_price=total_price,order_status_enum=OrderStatus.ORDER_PLACED,user_id=user_id,order_line_items=lst)

            db.session.add(order)
            db.session.commit()
            user.orders.append(order)

            for item in lst:
                item.order_id = order.id
        
            return order
        
        except IntegrityError as ex:
            print(ex)
            db.session.rollback()
            raise ValueError("Transaction did not go through!")
        except Exception as ex:
            print("Error:", ex)
            return None
        


    
    @staticmethod
    def get_inventory_item(item_id):
        item = InventoryItem.query.get(item_id)
        if item:
            return item
        return None