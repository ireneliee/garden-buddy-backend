from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from enum import Enum
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()

class OrderStatus(Enum):
    ORDER_PLACED = 'ORDER_PLACED'
    IN_TRANSIT = 'IN_TRANSIT'
    DELIVERED = 'DELIVERED'

class Environment(Enum):
    FOREST = 'FOREST'
    TROPICAL_RAINFOREST = 'TROPICAL_RAINFOREST'
    DESERT = 'DESERT'    
    MOUNTAIN = 'MOUNTAIN'    
    TROPICAL_FARM = 'TROPICAL_FARM'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False) 
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    user_start_date = db.Column(db.DateTime, nullable=False) 

    # One-to-many relationship with GardenBuddy
    garden_buddies = relationship('GardenBuddy', back_populates='user')
    orders = relationship('Order', back_populates='user')


    def __repr__(self):
        return f'<User {self.firstname} {self.lastname} {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'user_start_date': self.user_start_date.strftime('%Y-%m-%d')
        }


class GardenBuddy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_registered = db.Column(db.DateTime, nullable=False)

    # Define user_id as a foreign key for the relationship with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='garden_buddies')

    # Define the one-to-many relationship with Garden
    garden = relationship('Garden', back_populates='garden_buddy')
    def __repr__(self):
        return f'<GardenBuddy {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'date_registered': self.date_registered,
        }


class Garden(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # One-to-one relationship with GardenBuddy
    garden_buddy_id = db.Column(db.Integer, db.ForeignKey('garden_buddy.id'), unique=True, nullable=False)
    garden_buddy = relationship('GardenBuddy', back_populates='garden')

    # Define the relationship with GardenType
    garden_type_id = db.Column(db.Integer, db.ForeignKey('garden_type.id'), nullable=False)
    garden_type = relationship('GardenType')

    # Define relationships with other models
    garden_images = relationship('GardenImage', back_populates='garden')
    garden_data = relationship('GardenData')


    def __repr__(self):
        return f'<Garden {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
        }
    
class GardenImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    garden_image_link = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False) 

    # One-to-many relationship with GardenBuddy
    garden_id = db.Column(db.Integer, db.ForeignKey('garden.id'), nullable=False)

    garden = relationship('Garden', back_populates='garden_images')

    def __repr__(self):
        return f'<Garden {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
        }
    
class GardenData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    soil_ph_level = db.Column(db.Integer, nullable=False)
    air_temperature = db.Column(db.Integer, nullable=False) 
    soil__salinity = db.Column(db.Integer, nullable=False)
    soil_moisture= db.Column(db.Integer, nullable=False)
    date_timestamp = db.Column(db.DateTime, nullable=False) 

    # Add foreign key to reference Garden
    garden_id = db.Column(db.Integer, db.ForeignKey('garden.id'), nullable=False)
    garden = relationship('Garden', back_populates='garden_data')

    def __repr__(self):
        return f'<GardenData {self.date_timestamp}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'soil_ph_level': self.soil_ph_level,
            'air_temperature': self.air_temperature,
            'soil__salinity': self.soil__salinity,
            'soil_moisture': self.soil_moisture,
            'date_timestamp': self.date_timestamp.strftime('%Y-%m-%d')
        }
    
class GardenType(db.Model): #suspicious
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(200), nullable=False)
    plant_description = db.Column(db.String(200), nullable=False) 
    ideal_ph_level= db.Column(db.Integer, nullable=False)
    ideal_temp_level= db.Column(db.Integer, nullable=False)
    ideal_moisture_level= db.Column(db.Integer, nullable=False)
    ideal_soil_salinity= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<GardenType {self.plant_name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'plant_name': self.plant_name,
            'plant_description': self.plant_description,
            'ideal_ph_level': self.ideal_ph_level,
            'ideal_temp_level': self.ideal_temp_level,
            'ideal_moisture_level': self.ideal_moisture_level,
            'ideal_soil_salinity': self.ideal_soil_salinity,
        }
    
class Order(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Integer, nullable=False)
    order_status_enum = db.Column(db.Enum(OrderStatus), nullable=False) 

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = relationship('User', back_populates='orders')
    order_line_items = relationship('OrderLineItem', back_populates='order')

    def __repr__(self):
        return f'<Order {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'total_price': self.total_price,
            'order_status_enum': self.order_status_enum,
        }

class OrderLineItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    sub_total = db.Column(db.Integer, nullable=False) 

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    inventory_item_id = db.Column(db.Integer, db.ForeignKey('inventory_item.id'), nullable=False)

    order = relationship('Order')
    inventory_item = relationship('InventoryItem')
    def __repr__(self):
        return f'<OrderLineItem {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'sub_total': self.sub_total,
        }
    


# class InventoryItem(db.Model): 
#     __tablename__ = 'inventory_item'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     price = db.Column(db.Integer, nullable=False)
#     quantity = db.Column(db.Integer, nullable=False) 
#     description = db.Column(db.String(200), nullable=False) 

#     @declared_attr
#     def __mapper_args__(cls):
#         return {'polymorphic_on': cls.type}

#     def __repr__(self):
#         return f'<InventoryItem {self.id}>'
    
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'price': self.price,
#             'quantity': self.quantity,
#             'description': self.description,
#         }
    
class InventoryItem(db.Model): 
    __tablename__ = 'inventory_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False) 
    description = db.Column(db.String(200), nullable=False) 

    type = db.Column(db.String(50))  # Define the 'type' attribute for polymorphic mapping

    __mapper_args__ = {
        'polymorphic_identity': 'inventory_item',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f'<InventoryItem {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'description': self.description,
        }
    
class GardenBuddyPack(InventoryItem): 
    __tablename__ = 'garden_buddy_pack'
    id = db.Column(db.Integer, db.ForeignKey('inventory_item.id'), primary_key=True)
    plant_name = db.Column(db.String(20), nullable=False)
    garden_buddy_pack_description = db.Column(db.String(200), nullable=False)
    environment_enum = db.Column(db.Enum(Environment), nullable=False)

    garden_type_id = db.Column(db.Integer, db.ForeignKey('garden_type.id'), nullable=False)  # Foreign key to GardenType

    garden_type = relationship('GardenType')

    __mapper_args__ = {'polymorphic_identity': 'garden_buddy_pack'}

    def __repr__(self):
        return f'<GardenBuddyPack {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'plant_name': self.plant_name,
            'garden_buddy_pack_description': self.garden_buddy_pack_description,
            'environment_enum': self.environment_enum,
        }

class Accessory(InventoryItem): 
    __tablename__ = 'accessory'
    id = db.Column(db.Integer, db.ForeignKey('inventory_item.id'), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': 'accessory'}

    def __repr__(self):
        return f'<Accessory {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
        }