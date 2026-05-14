from src.utilities.extension import db, jwt
import os
# from flask_uuid import FlaskUUID
def connect_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
    # FlaskUUID(app)
    db.init_app(app)
    jwt.init_app(app)
    try:
        with app.app_context():
            db.create_all() 
        print("Database connected and tables created successfully!")
    except Exception as e:
        print(f"Error connecting to database: {e}")


    