from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
  id : Optional[int]
  username : str
  email : str
  password : str
  is_staff : Optional[bool]
  is_active : Optional[bool]

  class Config:
    orm_mode: True
    json_schema_extra={
      'example':{
        'username':'mohirdev',
        'email':'mohirdev.praktikum@gmail.com',
        'password':'password12345',
        'is_staff': False,
        'is_active': True
      }
    }

class Settings(BaseModel):
  authjwt_secret_key : str = '8f1afb841beab5da9a807cb2dc1eb4a173264f081b09d2039c5b5addc24e66eb'

class LoginModel(BaseModel):
  username : str
  password : str

  class Config:
    orm_mode: True
    json_schema_extra={
      'example':{
        'username':'mohirdev',
        'password':'mohirdev@123',
      }
    }