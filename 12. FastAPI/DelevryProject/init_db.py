from database import engine, Base
from models import Users, Orders, Product

Base.metadata.create_all(bind=engine)