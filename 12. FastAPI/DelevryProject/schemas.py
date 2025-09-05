from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
  id : Optional[int]
  username : str
  email : str
  password : str
  is_staff : Optional[bool]
  is_active : Optional[bool]

  # Eskirgan usul

  # class Config:
  #   orm_mode = True
  #   json_schema_extra={
  #     'example':{
  #       'username':'mohirdev',
  #       'email':'mohirdev.praktikum@gmail.com',
  #       'password':'password12345',
  #       'is_staff': False,
  #       'is_active': True
  #     }
  #   }

  # Yangi usul
  model_config = {
    "from_attributes": True,
    "json_schema_extra": {
            "example": {
              'username':'mohirdev',
              'email':'mohirdev.praktikum@gmail.com',
              'password':'password12345',
              'is_staff': False,
              'is_active': True
            }
        }
    }

class Settings(BaseModel):
  authjwt_secret_key : str = '8f1afb841beab5da9a807cb2dc1eb4a173264f081b09d2039c5b5addc24e66eb'

class LoginModel(BaseModel):
  username_or_email : str
  password : str

  # old
  # class Config:
  #   orm_mode = True
  #   json_schema_extra={
  #     'example':{
  #       'username':'mohirdev',
  #       'password':'mohirdev@123',
  #     }
  #   }

  # Yangi usul
  model_config = {
    "from_attributes": True,
    "json_schema_extra": {
            "example": {
              'username':'mohirdev',
              'password':'mohirdev@123',
            }
        }
    }

class OrderModel(BaseModel):
  id : Optional[int]
  quantity : int
  order_statuses : Optional[str] = "PENDING"
  user_id: Optional[int]
  product_id: Optional[int]
  # old
  # class Config:
  #   orm_mode = True
  #   json_schema_extra={
  #     'example':{
  #       'quantity':2,
  #     }
  #   }

  model_config = {
  "from_attributes": True,
  "json_schema_extra": {
          "example": {
            'quantity':2,
          }
      }
  }

class OrderStatusModel(BaseModel):
  order_statuses : Optional[str] = "PENDING"

# old
  # class Config:
  #   orm_mode = True
  #   json_schema_extra={
  #     'example':{
  #       'order_statuses' : "PENDING",
  #     }
  #   }

  # new
  model_config = {
  "from_attributes": True,
  "json_schema_extra": {
          "example": {
            'order_statuses' : "PENDING",
          }
      }
  }

class ProductModel(BaseModel):
  id : Optional[int]
  name : str
  price : str


  model_config = {
  "from_attributes": True,
  "json_schema_extra": {
          "example": {
            'name' : 'O\'zbekcha osh',
            'price' : 35000,
          }
      }
  }