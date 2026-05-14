from sqlite3 import IntegrityError
import uuid
from .model import User, db
from flask_jwt_extended import create_access_token
import gladiator as gl

class UserService:
    @staticmethod
    def register_user(username, email, password):
        if not all([username, email, password]):
            raise ValueError("Missing required username, email or password")
        data = {
            "username": username,
            "email": email,
            "password": password
        }
        rules = (
            ("username", gl.length_min(3), gl.length_max(50), gl.required),
            ("email", gl.format_email, gl.required),
            ("password", gl.required, gl.regex_('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,128}$'))
        )
        is_valid = gl.validate(rules, data)

        if not is_valid:
            error_messages = [f'Invalid {field}: {", ".join(errors)}' for field, errors in is_valid.errors]
            raise ValueError("Data validation failed: " + str(error_messages))
        
        if User.query.filter_by(username=username).first():
            raise IntegrityError("Username already exists")
        if User.query.filter_by(email=email).first():
            raise IntegrityError("Email already exists")
        
      
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        return {"message": "User registered successfully"}


    @staticmethod
    def authenticate_user(email, password):
        if not all([email, password]):
            return {"message": "Missing required email or password"}, 400
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity= str(user.user_id))
            return {"access_token": access_token}, 200
        return {"message": "Invalid email or password"}, 401


    @staticmethod
    def remove_user(user_id):
        if not user_id:
            raise ValueError({"message": "User ID is required"})        
        user = User.query.get(uuid.UUID(user_id))
        print(f"User found for deletion: {user}")
        if not user:
            raise ValueError({"message": "User not found"})
        db.session.delete(user)
        db.session.commit()
        return {"message": "User removed successfully"}
    
    @staticmethod
    def logout_user():
        # In a real application, you would handle token revocation here
        return {"message": "User logged out successfully"}, 200


