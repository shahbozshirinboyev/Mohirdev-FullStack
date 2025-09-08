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
    quantity=order.quantity,
    product_id=order.product_id,
    user_id=user.id
)

  session.add(new_order)
  session.commit()

  data = {
    'success': True,
    'code': 201,
    'message': 'Order is created successfully',
    "product": {
      "id": new_order.product.id,
      "name": new_order.product.name,
      "price": new_order.product.price
    },
    'data': {
      "id": new_order.id,
      "quantity": new_order.quantity,
      "order_statuses": new_order.order_statuses,
      "total_price": new_order.quantity * new_order.product.price
    }
  }

  return jsonable_encoder(data)

@order_router.get('/list', status_code=status.HTTP_200_OK)
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
            "id": order.user.id if order.user else None,
            "username": order.user.username if order.user else None,
            "email": order.user.email if order.user else None,
            "is_active": order.user.is_active if order.user else None,
            "is_staff": order.user.is_staff if order.user else None
        },
        "product": {
            "id": order.product.id if order.product else None,
            "name": order.product.name if order.product else None,
            "price": order.product.price if order.product else None
        } if order.product else None,
        'quantity': order.quantity,
        'order_statuses': order.order_statuses.value,
        "total_price": order.quantity * (order.product.price if order.product else 0)
    }
    for order in orders
]

    return jsonable_encoder(custom_data)
  else:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Superuser can see all orders.")

@order_router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_order_by_id(id:int, Authorize: AuthJWT=Depends()):

  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  user = Authorize.get_jwt_subject()
  current_user = session.query(Users).filter(Users.username==user).first()

  if current_user.is_staff:
    order = session.query(Orders).filter(Orders.id==id).first()
    if order:
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
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with ID={id} is not found.")
  else:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Superuser is allowed to this request.")

@order_router.get('/user/orders', status_code=status.HTTP_200_OK)
async def get_user_orders(Authorize:AuthJWT=Depends()):
  # get a requested user's orders.
  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  username = Authorize.get_jwt_subject()
  user = session.query(Users).filter(Users.username == username).first()
  custom_data = [
    {
        'id': order.id,
        'user': {
            "id": order.user.id if order.user else None,
            "username": order.user.username if order.user else None,
            "email": order.user.email if order.user else None,
            "is_active": order.user.is_active if order.user else None,
            "is_staff": order.user.is_staff if order.user else None
        },
        "product": {
            "id": order.product.id if order.product else None,
            "name": order.product.name if order.product else None,
            "price": order.product.price if order.product else None
        } if order.product else None,
        'quantity': order.quantity,
        'order_statuses': order.order_statuses.value,
        "total_price": order.quantity * (order.product.price if order.product else 0)
    }
    for order in user.orders
]
  return jsonable_encoder(custom_data)

@order_router.get('/user/{id}', status_code=status.HTTP_200_OK)
async def get_user_order_by_id(id:int, Authorize:AuthJWT=Depends()):
  # get user order by id
  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  username = Authorize.get_jwt_subject()
  current_user = session.query(Users).filter(Users.username == username).first()
  order = session.query(Orders).filter(Orders.id == id, Orders.user == current_user).first()
  # orders = current_user.orders
  if order:
    order_data = {
      'id': order.id,
      'user': {
          "id": order.user.id if order.user else None,
          "username": order.user.username if order.user else None,
          "email": order.user.email if order.user else None,
          "is_active": order.user.is_active if order.user else None,
          "is_staff": order.user.is_staff if order.user else None
      },
      "product": {
          "id": order.product.id if order.product else None,
          "name": order.product.name if order.product else None,
          "price": order.product.price if order.product else None
      } if order.product else None,
      'quantity': order.quantity,
      'order_statuses': order.order_statuses.value,
      "total_price": order.quantity * (order.product.price if order.product else 0)
    }
    return jsonable_encoder(order_data)
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No order with this ID={id}")

@order_router.put('/{id}/update', status_code=status.HTTP_200_OK)
async def update_order(id: int, order: OrderModel, Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

    order_to_update = session.query(Orders).filter(Orders.id == id).first()
    if not order_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found.")

    username = Authorize.get_jwt_subject()
    user = session.query(Users).filter(Users.username == username).first()

    # foydalanuvchi tekshiruvi
    if order_to_update.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You cannot update another user's order.")

    # maydonlarni yangilash
    order_to_update.quantity = order.quantity
    order_to_update.product_id = order.product_id
    if order.order_statuses:
        order_to_update.order_statuses = order.order_statuses

    session.commit()
    session.refresh(order_to_update)

    custom_response = {
        "success": True,
        "code": 200,
        "message": "Sizning buyurtmangiz muvaffaqiyatli o'zgartirildi.",
        "data": {
            "id": order_to_update.id,
            "quantity": order_to_update.quantity,
            "product": order_to_update.product_id,
            "order_status": order_to_update.order_statuses
        }
    }

    return jsonable_encoder(custom_response)
