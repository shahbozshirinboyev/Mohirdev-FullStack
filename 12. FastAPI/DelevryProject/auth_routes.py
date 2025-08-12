from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from schemas import SignUpModel
from database import session, engine
from models import Users

auth_router = APIRouter(
  prefix='/auth'
)

@auth_router.get('/')
async def auth():
  return {'message': 'Bu auth route signup sahifasi.'}

@auth_router.post('/signup/')
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
    password=user.password,
    is_staff=user.is_staff,
    is_active=user.is_active
  )