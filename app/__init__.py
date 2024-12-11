from flask import Flask
from app.routes import main_routes
from app.product_routes import product_routes
from app.category_routes import category_routes
from app.auth_routes import auth_routes
def create_app():
  app=Flask(__name__)
  app.secret_key = 'secret_key'
  app.register_blueprint(main_routes)
  app.register_blueprint(product_routes)
  app.register_blueprint(category_routes)
  app.register_blueprint(auth_routes)
  return app

