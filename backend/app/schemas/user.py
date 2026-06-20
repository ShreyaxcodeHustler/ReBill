from pydantic import BaseModel
from pydantic import EmailStr

class UserRegister(BaseModel):
    name:str
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    id :int
    name: str
    email :str
    class Config:
        from_attributes =True
