from flask import Blueprint, jsonify, request
from users.daos.user_dao import add_user, get_user_by_name


users_bp = Blueprint('users_bp', __name__)


@users_bp.route('', methods=['POST'])
def bp_add_user():
    add_user(request.json['username'], request.json['email'])
    stored_user = get_user_by_name(request.json['username'])
    return jsonify({'id': stored_user.id, 'username': stored_user.username, 'email': stored_user.email})


@users_bp.route('/<string:name>', methods=['GET'])
def bp_get_user(name):
    stored_user = get_user_by_name(name)
    return jsonify({'id': stored_user.id, 'username': stored_user.username, 'email': stored_user.email})

