from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import Users, Product, Orders
from schemas import OrderModel, OrderStatusModel
from database import session, engine
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, status

order_router = APIRouter(
  prefix='/order'
)

@order_router.get('/')
async def welcome_page(Authorize: AuthJWT=Depends()):

  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  return {'message': 'Bu order route buyurtmalar sahifasi sahifasi.'}

# @order_router.get('/')
# async def order():
#   pass