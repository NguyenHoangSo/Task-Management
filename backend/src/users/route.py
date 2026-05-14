from flask import Blueprint, current_app
from .controller import UserController
import logging
import uuid
api_bp = Blueprint('api', __name__, url_prefix='/api/auth')

@api_bp.route('/register', methods=['POST'])
def register():
    return UserController.register()
@api_bp.route('/login', methods=['POST'])
def login():
    return UserController.login()

@api_bp.route('/user/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)

