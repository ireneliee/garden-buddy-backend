from flask import  render_template
from ..services.GardenService import GardenService

def setup_app_routes(app):
  @app.route('/')
  def index():
      return render_template('index.html')

  @app.route('/mlactions')
  def mlActions():
      return render_template('mlActions.html')
  
  @app.route('/gardenTypes')
  def gardenTypes():
      garden_types = GardenService.get_all_garden_types()
      return render_template('allGardenType.html', garden_types = garden_types)

