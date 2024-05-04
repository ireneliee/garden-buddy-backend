from flask import  render_template
from ..services.GardenService import GardenService

def setup_app_routes(app):
    @app.route('/')
    def index():
        garden_types = GardenService.get_all_garden_types()
        return render_template('index.html', title="Garden Buddy Homepage", content="I love Garden Buddy", garden_types=garden_types)

