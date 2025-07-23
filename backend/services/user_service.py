from sqlalchemy.orm import Session
from schemas import UserCreate, User
from models import User as UserModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = pwd_context.hash(user.password)
    db_user = UserModel(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return User.from_orm(db_user)

def get_user(db: Session, user_id: int) -> User | None:
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user:
        return User.from_orm(db_user)
    return None
