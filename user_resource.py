from flask import Blueprint, jsonify
from uuid import uuid4

user_path = Blueprint('user', __name__, url_prefix='/user')

@user_path.route('/create/', methods=['PUT'])
def create_user(user):
    return None

@user_path.route('/list/', methods=['GET'])
def list_user():
    return jsonify([
        {
            'id': str(uuid4()),
            'name': 'Obi-Wan Kenobi',
            'email': 'obiwan@jedi.sw',
            'active': 1},
        {
            'id': str(uuid4()),
            'name': 'Anakin Skywalker',
            'email': 'darth@imperial.sw',
            'active': 1
        }
    ]), 200

@user_path.route('/login/', methods=['POST'])
def do_login(user):
    return None