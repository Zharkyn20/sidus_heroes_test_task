from sqlalchemy import Column, Integer, String, UniqueConstraint

from user.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint("username", "email", name="_username_email_uc"),)
