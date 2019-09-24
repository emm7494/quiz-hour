import os
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler
from flask import Flask


def create_app(config_class):
    app = Flask(__name__, static_url_path="")
    app.config.from_object(config_class)

    # Importing blueprints
    from .main import bp as main_bp

    # Registering blueprints
    app.register_blueprint(main_bp)

    # Logging errors to file
    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = RotatingFileHandler(
        "logs/quiz_hour.log", maxBytes=10240, backupCount=10
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s:%(message)s [in %(pathname)s: %(lineno)d]"
        )
    )
    app.logger.info("Quiz Hour is running...")
    return app
