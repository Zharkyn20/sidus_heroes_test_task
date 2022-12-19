from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends

from user.schemas.user import CreateUser, ShowUser, UpdateUser
from user.db.session import get_db
from user.db.repository.user import (
    create_new_user,
    get_user_by_email_or_username,
    get_user_by_id,
    update_user_by_id,
)

router = APIRouter()


@router.post(
    "/create-user", response_model=ShowUser, status_code=status.HTTP_201_CREATED
)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    get_user_by_email_or_username(email=user.email, username=user.username, db=db)

    user = create_new_user(user=user, db=db)
    return user


@router.get("/user/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
def read_user(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(id=id, db=db)

    return user


@router.put("/user/{id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
def update_user(id: int, user: UpdateUser, db: Session = Depends(get_db)):
    new_user = update_user_by_id(id=id, user=user, db=db)

    return new_user
