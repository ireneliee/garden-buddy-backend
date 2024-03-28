from .config import Config
from .models import db, User
from .services.UserService import UserService
from .services.GardenService import GardenService
from .services.ShopService import ShopService
from .routes import AppRoute, UserRoute, GardenRoute
import connexion

from sqlalchemy import inspect

# Load configuration
config = Config()

# Initialize connexion app
app = connexion.App(__name__, specification_dir='./')

# Add the API specification
app.add_api('openapi/swagger.yml')
# app.add_api('swagger.yml')

# Configure Flask app using Connexion's underlying Flask app
flask_app = app.app
flask_app.config.from_object(config)

# Initialize database
db.init_app(flask_app)

# Drop all tables in the database if they exist
with flask_app.app_context():
    db.drop_all()

# dataloader method (consider refactoring)
def create_sample_users():
    print("Creating sample users")
    users = [
        {'username': 'user1', 'password': 'password1', 'firstname': 'John', 'lastname': 'Doe'},
        {'username': 'user2', 'password': 'password2', 'firstname': 'Jane', 'lastname': 'Smith'}
    ]
    for user_data in users:
        user = UserService.create_user(**user_data)
        print(f"Created user: {user}")

def create_sample_garden_types():
    print("Creating garden types")
    #  def create_garden_type(plant_name, plant_description, ideal_ph_level, ideal_temp_level, ideal_moisture_level, ideal_soil_salinity):

    types = [
        {'plant_name': 'Rose', 'plant_description': 'Roses are woody perennial flowering plants of the genus Rosa, in the family Rosaceae, or the flower it bears.', 'ideal_ph_level': 6.0, 'ideal_temp_level': 20, 'ideal_moisture_level': 50, 'ideal_soil_salinity': 20},
        {'plant_name': 'Lavender', 'plant_description': 'Lavender is a flowering plant in the mint family Lamiaceae, native to the Mediterranean region.', 'ideal_ph_level': 6.5, 'ideal_temp_level': 25, 'ideal_moisture_level': 40, 'ideal_soil_salinity': 15},
        {'plant_name': 'Tomato', 'plant_description': 'The tomato is the edible berry of the plant Solanum lycopersicum, commonly known as a tomato plant.', 'ideal_ph_level': 6.0, 'ideal_temp_level': 22, 'ideal_moisture_level': 60, 'ideal_soil_salinity': 10},
        {'plant_name': 'Sunflower', 'plant_description': 'Helianthus annuus, the common sunflower, is a large annual forb of the genus Helianthus grown as a crop for its edible oil and edible fruits.', 'ideal_ph_level': 6.5, 'ideal_temp_level': 25, 'ideal_moisture_level': 60, 'ideal_soil_salinity': 10},
        {'plant_name': 'Basil', 'plant_description': 'Basil, also called great basil, is a culinary herb of the family Lamiaceae.', 'ideal_ph_level': 6.0, 'ideal_temp_level': 20, 'ideal_moisture_level': 70, 'ideal_soil_salinity': 15},
        {'plant_name': 'Cactus', 'plant_description': 'Cacti are succulent plants in the family Cactaceae.', 'ideal_ph_level': 6.5, 'ideal_temp_level': 30, 'ideal_moisture_level': 20, 'ideal_soil_salinity': 25},
        {'plant_name': 'Orchid', 'plant_description': 'Orchids are a diverse and widespread family of flowering plants.', 'ideal_ph_level': 5.5, 'ideal_temp_level': 20, 'ideal_moisture_level': 70, 'ideal_soil_salinity': 20},
        {'plant_name': 'Fern', 'plant_description': 'Ferns are a group of vascular plants that reproduce via spores and have neither seeds nor flowers.', 'ideal_ph_level': 6.0, 'ideal_temp_level': 18, 'ideal_moisture_level': 80, 'ideal_soil_salinity': 15},
        {'plant_name': 'Pineapple', 'plant_description': 'The pineapple is a tropical plant with edible multiple fruit consisting of coalesced berries.', 'ideal_ph_level': 5.5, 'ideal_temp_level': 25, 'ideal_moisture_level': 60, 'ideal_soil_salinity': 10},
        {'plant_name': 'Rosemary', 'plant_description': 'Rosemary is a fragrant evergreen herb native to the Mediterranean.', 'ideal_ph_level': 6.5, 'ideal_temp_level': 22, 'ideal_moisture_level': 50, 'ideal_soil_salinity': 20}
    ]
    for gardenType in types:
        gType = GardenService.create_garden_type(**gardenType)
        print(f"Created GardenType: {gType}")

def create_sample_items():
    print("Creating sample items")

    # Sample garden buddy packs
    garden_buddy_packs = [
        {
            'name': 'Lavender Garden Set',
            'price': 30,
            'quantity': 8,
            'description': 'A complete set for growing beautiful lavender plants',
            'plant_name': 'Lavender',
            'garden_buddy_pack_description': 'Includes seeds, pots, soil, and fertilizer for lavender plants',
            'environment_enum': 'DESERT',  # Adjust environment_enum as needed
            'garden_type_id': 3  # Adjust garden_type_id as needed
        },
        {
            'name': 'Cactus Collection',
            'price': 25,
            'quantity': 12,
            'description': 'Assorted cactus plants for indoor decoration',
            'plant_name': 'Cactus',
            'garden_buddy_pack_description': 'Includes a variety of small cactus plants and decorative pots',
            'environment_enum': 'TROPICAL_FARM',  # Adjust environment_enum as needed
            'garden_type_id': 4  # Adjust garden_type_id as needed
        }
    ]

    # Sample accessories
    accessories = [
        {
            'name': 'Watering Can',
            'price': 15,
            'quantity': 25,
            'description': 'A durable watering can for watering plants'
        },
        {
            'name': 'Garden Trowel',
            'price': 12,
            'quantity': 18,
            'description': 'A handheld garden tool for digging and planting'
        },
        {
            'name': 'Plant Mister',
            'price': 8,
            'quantity': 20,
            'description': 'A convenient plant mister for gentle watering'
        },
        {
            'name': 'Pruning Shears',
            'price': 20,
            'quantity': 15,
            'description': 'Sharp pruning shears for trimming plants'
        },
        {
            'name': 'Garden Gloves',
            'price': 10,
            'quantity': 30,
            'description': 'Protective gloves for gardening tasks'
        },
        {
            'name': 'Plant Labels',
            'price': 5,
            'quantity': 40,
            'description': 'Markers for labeling plants in the garden'
        },
        {
            'name': 'Seed Starter Kit',
            'price': 18,
            'quantity': 10,
            'description': 'All-in-one kit for starting seeds indoors'
        },
        {
            'name': 'Garden Kneeler',
            'price': 25,
            'quantity': 8,
            'description': 'Padded kneeler for comfortable gardening'
        },
        {
            'name': 'Hand Rake',
            'price': 12,
            'quantity': 20,
            'description': 'Small rake for cleaning up debris in the garden'
        },
        {
            'name': 'Plant Stand',
            'price': 30,
            'quantity': 15,
            'description': 'Decorative stand for displaying potted plants'
        }
    ]

    # Create garden buddy packs
    for pack_data in garden_buddy_packs:
        item = ShopService.create_garden_buddy_pack(**pack_data)
        print(f"Created Garden Buddy Pack: {item}")

    # Create accessories
    for accessory_data in accessories:
        item = ShopService.create_accessory(**accessory_data)
        print(f"Created Accessory: {item}")

# dataloader and init db
with flask_app.app_context():
    inspector = inspect(db.engine)
    if not inspector.has_table(User.__tablename__):
        db.create_all()
        create_sample_users()
        create_sample_garden_types()
        create_sample_items()

# load in routes
AppRoute.setup_app_routes(flask_app)
UserRoute.setup_user_routes(flask_app)
GardenRoute.setup_garden_routes(flask_app)

# run app
if __name__ == '__main__':
    app.run(port=5000)
