from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import Users, Product, Orders
from schemas import ProductModel, OrderModel
from database import session, engine
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, status

product_router = APIRouter( prefix='/product' )
session = session(bind=engine)

@product_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductModel, Authorize: AuthJWT=Depends()):
  # create a new product endpoint
  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  user = Authorize.get_jwt_subject()
  current_user = session.query(Users).filter(Users.username == user).first()

  if current_user.is_staff:
    new_product = Product(
      name=product.name,
      price=product.price
    )
    session.add(new_product)
    session.commit()
    data = {
      "success": True,
      "code": 201,
      "message": "Product is created successfully",
      "data": {
        "id": new_product.id,
        "name": new_product.name,
        "price": new_product.price
      }
    }
    return jsonable_encoder(data)
  else:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin can add new product.")

@product_router.get('/list', status_code=status.HTTP_200_OK)
async def list_all_products(Authorize: AuthJWT=Depends()):
  # This route return all product list
  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  user = Authorize.get_jwt_subject()
  current_user = session.query(Users).filter(Users.username == user).first()

  if current_user.is_staff:
    products = session.query(Product).all()
    custom_data = [
      {
        "id": product.id,
        "name": product.name,
        "price": product.price
      }
      for product in products
    ]
    return jsonable_encoder(custom_data)
  else:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin can see all products.")

@product_router.get('/{id}',  status_code=status.HTTP_200_OK)
async def get_product_by_id(id:int, Authorize: AuthJWT=Depends()):

  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  user = Authorize.get_jwt_subject()
  current_user = session.query(Users).filter(Users.username==user).first()

  if current_user.is_staff:
    product = session.query(Product).filter(Product.id==id).first()
    if product:
      custom_product = {
          'id': product.id,
          'name': product.name,
          'price': product.price,
        }
      return jsonable_encoder(custom_product)
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID={id} is not found.")
  else:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Superuser is allowed to this request.")

@product_router.delete('/{id}',  status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_by_id(id:int, Authorize:AuthJWT=Depends()):
  # This endpoint delete product use ID.

  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter valid access token.")

  user = Authorize.get_jwt_subject()
  current_user = session.query(Users).filter(Users.username==user).first()

  if current_user.is_staff:
    product = session.query(Product).filter(Product.id==id).first()
    if product:
      session.delete(product)
      session.commit()
      data = {
        "success": True,
        "code": 200,
        "message": f"Product with ID={id} has been delete.",
        "data": None

      }
      return jsonable_encoder(data)
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID={id} is not found.")
  else:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only Superuser is allowed to delete product.")

@product_router.put('/{id}/update', status_code=status.HTTP_200_OK)
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

    if order_to_update.user != user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You cannot update another user's order.")

    # update fields
    order_to_update.quantity = order.quantity
    order_to_update.product_id = order.product_id
    if order.order_statuses:  # agar kelgan bo‘lsa
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