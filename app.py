from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dev.db'

    if test_config is not None:
        app.config.from_mapping(test_config)

    db.init_app(app)

    @app.route('/users', methods=['POST'])
    def add_user():
        user = User({'username': request.json['username'], 'email': request.json['email']})
        db.session.add(user)
        db.session.commit()
        stored_user = User.query.filter_by(username='admin').first()
        return jsonify({'id': stored_user.id, 'username': stored_user.username, 'email': stored_user.email})

    return app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
