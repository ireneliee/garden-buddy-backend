from flask import  render_template

def setup_app_routes(app):
  @app.route('/')
  def index():
      return render_template('index.html')

  @app.route('/mlactions')
  def mlActions():
      return render_template('mlActions.html')

