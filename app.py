from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dev.db'

    if test_config is not None:
        app.config.from_mapping(test_config)

    db.init_app(app)

    from users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app



