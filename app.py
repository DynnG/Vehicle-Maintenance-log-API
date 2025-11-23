from flask import Flask
from config import Config
from models import db
from services.auth_service import bcrypt
from flask_jwt_extended import JWTManager

import logging
import os

# Blueprints
from controllers.auth_controller import auth_bp
from controllers.log_controller import log_bp

app = Flask(__name__)
app.config.from_object(Config)

# Init extensions
db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)

# Logging setup
os.makedirs(app.config['LOG_FOLDER'], exist_ok=True)
logging.basicConfig(
    filename=f"{app.config['LOG_FOLDER']}/app.log",
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(log_bp, url_prefix="/logs")

# Create database
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
