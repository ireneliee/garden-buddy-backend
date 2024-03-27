from flask import  render_template

def setup_app_routes(app):
  @app.route('/')
  def index():
      return render_template('index.html', title="Garden Buddy Homepage", content="I love Garden Buddy")

