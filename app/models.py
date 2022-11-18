from app.db import Base

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    location_decoration_array = Column(String, nullable=False)
    description = Column(String, nullable=False)

    price_expires_date = Column(TIMESTAMP(timezone=True), nullable=True)
    product_marketing_point_array = Column(String, nullable=True)
    product_keyword_array = Column(String, nullable=True)
    product_brand = Column(String, nullable=True)
    
    export = Column(Boolean, nullable=False)

    product_category_array = Column(String, nullable=True)
    related_product_array = Column(String, nullable=True)

    product_part_array = Column(String, nullable=False)
    last_change_date = Column(Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')))
    creation_date = Column(Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')))
    end_date = Column(TIMESTAMP(timezone=True), nullable=True)
    effective_date = Column(TIMESTAMP(timezone=True), nullable=True)
    is_caution = Column(Boolean, nullable=False)
    caution_comment = Column(String, nullable=True)
    is_closeout = Column(Boolean, nullable=False)
    line_name = Column(String, nullable=True)
    primary_img_url = Column(String, nullable=True)
    
    primary_img_url = Column(String, nullable=True)
    primary_img_url = Column(String, nullable=True)
    primary_img_url = Column(String, nullable=True)
    primary_img_url = Column(String, nullable=True)
    primary_img_url = Column(String, nullable=True)
    primary_img_url = Column(String, nullable=True)
    primary_img_url = Column(String, nullable=True)
    


    

