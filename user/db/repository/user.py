from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from user.schemas.user import CreateUser
from user.db.models.user import User
from user.core.hashing import Hasher


def create_new_user(user: CreateUser, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user_by_id(id: int, user: User, db: Session):
    to_update = db.query(User).filter(User.id == id)

    if not to_update.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id: {id} does not exists",
        )
    get_user_by_email_or_username(email=user.email, username=user.username, db=db)
    new_user_params = user.dict(exclude_none=True)
    new_password = new_user_params.pop("password")
    to_update.hashed_password = Hasher.get_password_hash(new_password)

    to_update.update(new_user_params, synchronize_session=False)
    db.commit()
    return user


def get_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id: {id} does not exists",
        )

    return user


def get_user_by_email_or_username(email: str, username: str, db: Session):
    user_by_email = db.query(User).filter(User.email == email).first()
    user_by_username = db.query(User).filter(User.username == username).first()

    if user_by_email or user_by_username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or Email already exists",
        )

    return None
