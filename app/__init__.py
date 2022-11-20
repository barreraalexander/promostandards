from flask import Flask, jsonify
from app.config import settings

def create_app(config_class=settings):
# def create_app():
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.blueprints.api.routes import router as api_router
    app.register_blueprint(api_router)


    return app