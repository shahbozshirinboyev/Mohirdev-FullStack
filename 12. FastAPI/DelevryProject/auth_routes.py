from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from schemas import SignUpModel, LoginModel
from database import session, engine
from models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_

auth_router = APIRouter(
  prefix='/auth'
)

session = session(bind=engine)

@auth_router.get('/')
async def auth(Authorize: AuthJWT=Depends()):
  try:
    Authorize.jwt_required()
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token.")
  return {'message': 'Bu auth route signup sahifasi.'}

@auth_router.post('/signup/', status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
  db_email = session.query(Users).filter(Users.email==user.email).first()
  if db_email is not None:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with  this email already exists.')

  db_username = session.query(Users).filter(Users.username==user.username).first()
  if db_username is not None:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with  this username already exists.')

  new_user = Users(
    username=user.username,
    email=user.email,
    password=generate_password_hash(user.password),
    is_staff=user.is_staff,
    is_active=user.is_active
  )

  session.add(new_user)
  session.commit()

  data = {
    "id": new_user.id,
    "username": new_user.username,
    "email": new_user.email,
    "is_active": new_user.is_active,
    "is_staff": new_user.is_staff,

  }
  response_model = {
    'success': True,
    'code': 201,
    'message': 'User is created successfully.',
    'data': data
  }

  return response_model

@auth_router.post('/login/', status_code=status.HTTP_200_OK)
async def login(user:LoginModel, Authorize:AuthJWT=Depends()):

  # Faqat username orqali login qilish
  # db_user = session.query(Users).filter(Users.username == user.username).first()

  # username or email orqali login qilish
  db_user = session.query(Users).filter(
    or_(
      Users.username == user.username_or_email,
      Users.email == user.username_or_email
    )
  ).first()

  if db_user and check_password_hash(db_user.password, user.password):
    access_token = Authorize.create_access_token(subject=db_user.username)
    refresh_token = Authorize.create_refresh_token(subject=db_user.username)

    token = {
      "access": access_token,
      "refresh": refresh_token
    }

    response = {
      'success': True,
      'code': 200,
      'message': 'User successfully login.',
      "data": token
    }

    return jsonable_encoder(response)
  raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid username or password.")