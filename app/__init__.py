from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or {})
    db.init_app(app)

    # blueprints
    from app.article.controllers import article
    app.register_blueprint(article)
    return app
