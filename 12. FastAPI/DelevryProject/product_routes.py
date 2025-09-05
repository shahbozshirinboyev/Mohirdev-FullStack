from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import Users, Product
from schemas import ProductModel
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