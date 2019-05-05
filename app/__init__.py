from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

load_dotenv()
db = SQLAlchemy()
ma = Marshmallow()


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or {})
    db.init_app(app)
    ma.init_app(app)

    # blueprints
    from app.article.controllers import article
    app.register_blueprint(article)
    return app
