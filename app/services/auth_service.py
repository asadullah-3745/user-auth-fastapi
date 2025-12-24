from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password


class AuthService:

    def create_user(self, db: Session, email: str, password: str):
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            raise ValueError("User already exists")

        user = User(
            email=email,
            hashed_password=hash_password(password) 
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def authenticate_user(self, db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None

        if not verify_password(password, user.hashed_password):  
            return None

        return user
