from app.database import Base

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class ProductData(Base):
    __tablename__ = 'products'

    product_id = Column(String, primary_key=True, nullable=False)
    product_name = Column(String, nullable=False)
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
    
    primary_image_url = Column(String, nullable=True)
    product_price_group_array = Column(String, nullable=True)
    compliance_info_available = Column(Boolean, nullable=True)
    unspsc_commodity_code = Column(Integer, nullable=True)
    imprint_size = Column(String, nullable=True)
    default_set_up_charge = Column(String, nullable=True)
    default_run_charge = Column(String, nullable=True)    
    fob_point_array = Column(String, nullable=False)

# inventory is just a composition of products
# class Inventory(Base):
#     __tablename__ = 'inventory'
#     pass

class MediaContent(Base):
    __tablename__ = 'media_content'
    product_id = Column(String, primary_key=True, nullable=False)
    part_id = Column(String, nullable=True)
    url = Column(String, nullable=False)
    media_type = Column(String, nullable=True)
    class_type_array = Column(String, nullable=False)
    file_size_ = Column(Float, nullable=True)
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    dpi = Column(Integer, nullable=True)
    color = Column(String, nullable=True)
    decoration_array = Column(String, nullable=True)
    location_array = Column(String, nullable=True)
    description = Column(String, nullable=True)
    single_part = Column(Boolean, nullable=False)
    change_time_stamp = Column(Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')))





class PPC(Base):
    __tablename__ = 'ppc'
    pass