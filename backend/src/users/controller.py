import uuid

from flask import request, jsonify
from .service import UserService
from sqlite3 import IntegrityError
class UserController:
    @staticmethod
    def register():
        data = request.get_json(force=True)
        try:
            response = UserService.register_user(data.get('username'), data.get('email'), data.get('password'))
        except ValueError as ve:
            return jsonify({"message": str(ve)}), 400
        except IntegrityError as ie:
            return jsonify({"message": str(ie)}), 409
        except Exception as e:
            return jsonify({"message": str(e)}), 500
        return jsonify(response), 201

    @staticmethod
    def login():
        data = request.get_json(force=True)
        email = data.get('email')
        password = data.get('password')
        response, status_code = UserService.authenticate_user(email, password)
        return jsonify(response), status_code
    
    @staticmethod
    def delete_user(user_id):
        try:
            print(f"Attempting to delete user with ID: {user_id} type: {type(user_id)}")
            response = UserService.remove_user(user_id)
            return jsonify(response), 204
        except ValueError as ve:
            print(f"ValueError: {ve}")
            return jsonify({"message": str(ve)}), 404
        except Exception as e:
            return jsonify({"message": str(e)}), 500