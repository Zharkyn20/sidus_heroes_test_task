from pydantic import BaseModel, EmailStr, validator


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    password2: str

    @validator("password2")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v


class ShowUser(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    username: str
    email: EmailStr
    password: str
