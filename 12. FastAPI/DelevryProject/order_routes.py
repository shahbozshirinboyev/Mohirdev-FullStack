from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import Users, Product, Orders
from schemas import OrderModel, OrderStatusModel
from database import session, engine
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, status

session = session(bind=engine)

order_router = APIRouter(
  prefix='/order'
)

@order_router.get('/')
async def welcome_page(Authorize: AuthJWT=Depends()):

  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  return {'message': 'Bu order route buyurtmalar sahifasi.'}

@order_router.post('/make', status_code=status.HTTP_201_CREATED)
async def make_order(order: OrderModel, Authorize: AuthJWT=Depends()):
  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  current_user = Authorize.get_jwt_subject()
  user = session.query(Users).filter(Users.username==current_user).first()

  new_order = Orders(
    quantity = order.quantity,
    # product = order.product_id
  )
  new_order.user = user
  session.add(new_order)
  session.commit()

  data = {
    'success': True,
    'code': 201,
    'message': 'Order is created successfully',
    'data': {
      "id": new_order.id,
      "quantity": new_order.quantity,
      "order_statuses": new_order.order_statuses
    }
  }

  return jsonable_encoder(data)

@order_router.get('/list')
async def list_order(Authorize: AuthJWT=Depends()):
  # This will return a list of all orders.
  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  current_user = Authorize.get_jwt_subject()
  user = session.query(Users).filter(Users.username == current_user).first()

  if user.is_staff:
    orders = session.query(Orders).all()
    custom_data = [
      {
        'id': order.id,
        'user': {
          "id": order.user.id,
          "username": order.user.username,
          "email": order.user.email,
          "is_active": order.user.is_active,
          "is_staff": order.user.is_staff
          },
        'product_id': order.product_id,
        'quantity': order.quantity,
        'order_statuses': order.order_statuses.value
      }
      for order in orders
    ]
    return jsonable_encoder(custom_data)
  else:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Superuser can see all orders.")

@order_router.get('/{id}')
async def get_order_by_id(id:int, Authorize: AuthJWT=Depends()):

  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  user = Authorize.get_jwt_subject()
  current_user = session.query(Users).filter(Users.username==user).first()

  if current_user.is_staff:
    order = session.query(Orders).filter(Orders.id==id).first()
    custom_order = {
        'id': order.id,
        'user': {
          "id": order.user.id,
          "username": order.user.username,
          "email": order.user.email,
          "is_active": order.user.is_active,
          "is_staff": order.user.is_staff
          },
        'product_id': order.product_id,
        'quantity': order.quantity,
        'order_statuses': order.order_statuses.value
      }
    return jsonable_encoder(custom_order)
  else:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Superuser is allowed to this request.")