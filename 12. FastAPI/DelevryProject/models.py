from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

# class Users(Base):
#   __tablename__ = 'users'
#   id = Column(Integer, primary_key=True)
#   username = Column(String(25), unique=True)
#   email = Column(String(70), nullable=True)
#   password = Column(Text, nullable=True)
#   is_staff = Column(Boolean, default=False)
#   is_active = Column(Boolean, default=False)
#   orders = relationship('Orders', back_populates='user')

#   def __repr__(self):
#     return f"<user {self.username}"

# class Orders(Base):
#   ORDER_STATUSES = (
#     ('PENDING', 'pending'),
#     ('IN_TRANSIT', 'in_transit'),
#     ('DELIVERED', 'delivered'),

#   )
#   __tablename__ = 'orders'
#   id = Column(Integer, primary_key=True)
#   quantity = Column(Integer, nullable=False)
#   order_statuses = Column(ChoiceType(choices=ORDER_STATUSES), default='PENDING')
#   user_id = Column(Integer, ForeignKey('users.id'))
#   user = relationship('Users', back_populates='orders')
#   product_id = Column(Integer, ForeignKey('product.id'))
#   product = relationship('Product', back_populates='orders')

#   def __repr__(self):
#     return f"<order {self.id}"

# class Product(Base):
#   __tablename__ = 'product'
#   id = Column(Integer, primary_key=True)
#   name = Column(String(100))
#   price = Column(Integer)

#   def __repr__(self):
#     return f"<product {self.name}"

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(70), nullable=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    orders = relationship('Orders', back_populates='user')  # ✅ 'user' ga o‘zgartirildi

    def __repr__(self):
        return f"<user {self.username}>"


class Orders(Base):
    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered'),
    )
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_statuses = Column(ChoiceType(choices=ORDER_STATUSES), default='PENDING')

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', back_populates='orders')  # ✅ 'orders' bilan mos

    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', back_populates='orders')  # ✅ Product’da ham 'orders' bo‘lishi kerak

    def __repr__(self):
        return f"<order {self.id}>"


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)

    orders = relationship('Orders', back_populates='product')  # ✅ Orders bilan mos

    def __repr__(self):
        return f"<product {self.name}>"
