from app.database import Base

from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

#PRODUCT DATA MODELS 
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
    last_change_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    creation_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
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



# MEDIA CONTENT MODELS
class MediaContent(Base):
    __tablename__ = 'media_content'

    product_id = Column(String, primary_key=True, nullable=False)
    part_id = Column(String, nullable=True)
    url = Column(String, nullable=False)
    media_type = Column(String, nullable=True)
    class_type_array = Column(String, nullable=False)
    file_size = Column(Float, nullable=True)
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    dpi = Column(Integer, nullable=True)
    color = Column(String, nullable=True)
    decoration_array = Column(String, nullable=True)
    location_array = Column(String, nullable=True)
    description = Column(String, nullable=True)
    single_part = Column(Boolean, nullable=False)
    change_time_stamp = Column(TIMESTAMP(timezone=True), nullable=True)
    


# PPC MODELS
class AvailableLocation(Base):
    __tablename__ = 'locations'
    location_id = Column(Integer, primary_key=True, nullable=False)
    location_name = Column(String, nullable=False)


class DecorationColor(Base):
    __tablename__ = 'decoration_colors'

    product_id = Column(String, primary_key=True, nullable=False)
    color_array = Column(String, nullable=False)
    location_id = Column(String, nullable=False)
    decoration_method_array = Column(String, nullable=False)
    pms_match = Column(Boolean, nullable=False)
    full_color = Column(Boolean, nullable=False)

class FobPoint(Base):
    __tablename__ = 'fob_points'

    fob_id = Column(String, primary_key=True, nullable=False)
    fob_postal_code = Column(String, nullable=False)
    fob_city = Column(String, nullable=False)
    fob_state = Column(String, nullable=False)
    fob_country = Column(String, nullable=False)
    currency_supported_array = Column(String, nullable=False)
    product_array = Column(String, nullable=False)

class LocationDecoration(Base):
    __tablename__ = 'location_decorations'

    location_name = Column(String, primary_key=True, nullable=False)
    max_imprint_colors = Column(Integer, nullable=True)
    decoration_name = Column(String, nullable=False)
    location_decoration_combo_default = Column(Boolean, nullable=False)
    price_includes = Column(Boolean, nullable=False)
    


class AvailableCharge(Base):
    __tablename__ = 'available_charges'

    charge_id = Column(Integer, primary_key=True, nullable=False)
    charge_name = Column(String, nullable=False)
    charge_type = Column(String, nullable=False)
    charge_description = Column(String, nullable=False)

class Configuration(Base):
    __tablename__ = 'configurations'

    part_array = Column(String, nullable=False)
    location_array = Column(String, nullable=False)
    product_id = Column(String, nullable=False, primary_key=True)
    currency = Column(String, nullable=False)
    fob_array = Column(String, nullable=False)
    fob_postal_code = Column(String, nullable=True)
    price_type = Column(String, nullable=True)
