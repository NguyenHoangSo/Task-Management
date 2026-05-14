from datetime import datetime
from src.utilities.extension import db
from sqlalchemy.orm import Mapped, mapped_column  
from sqlalchemy import Uuid
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
class User(db.Model):
    __tablename__ = 'user'
    user_id: Mapped[uuid.uuid4] = mapped_column(Uuid(native_uuid=False),primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(128), nullable=False)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, server_default=db.func.now(), nullable=True)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}', email='{self.email}')>"


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
