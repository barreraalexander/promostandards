from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Color(BaseModel):
    color_name: str
    hex: Optional[str]
    approximate_pms: Optional[str]
    standard_color_name: Optional[str]


class Specification(BaseModel):
    pass

class ApparelSize(BaseModel):
    pass

class Dimension(BaseModel):
    pass

class Decoration(BaseModel):
    decoration_id: int
    decoration_name: str

class Location(BaseModel):
    location_id: int
    location_name: str

class Part(BaseModel):
    pass

class ProductMarketingPoint(BaseModel):
    point_type: Optional[str]
    point_copy: str

class ProductKeyword(BaseModel):
    keyword: str

class RelatedProduct(BaseModel):
    relation_type: str
    product_id: str
    part_id: Optional[str]

class ProductPackaging(BaseModel):
    pass

class ShippingPackaging(BaseModel):
    pass

class ProductPart(BaseModel):
    part_id: str
    description: Optional[str]
    country_of_origin: Optional[str]
    color_array: List[Color]
    primary_material: Optional[str]
    specification_array: List[Specification]
    shape: Optional[str]
    apparel_size: Optional[ApparelSize]
    dimension: Optional[Dimension]
    lead_time: Optional[int]
    unspsc: Optional[str]
    gtin: Optional[str]
    is_rush_service: bool
    product_packaging_array: List[ProductPackaging]
    shipping_packaging_array: List[ShippingPackaging]
    end_date: Optional[datetime]
    effective_date: Optional[datetime]
    is_closeout: bool
    is_caution: bool
    caution_comment: Optional[str]
    nmfc_code: Optional[float]
    nmfc_description: Optional[str]
    is_on_demand: bool
    is_hazmat: bool
    primary_color: Optional[Color]


class FobPoint(BaseModel):
    fob_id: str
    fob_postal_code: str
    fob_city: str
    fob_state: str
    fob_country: str

class ProductCategory(BaseModel):
    category: str
    sub_category: str

class ProductPriceGroup(BaseModel):
    group_name: str
    currency: str
    description: Optional[str]
    product_price_array: List[str]






# class ProductMarketingPoint(BaseModel):
#     point_type: Optional[str]
#     poin



class ProductDataBase(BaseModel):
    product_id: str
    product_name: str
    location_decoration_array: List[Decoration]
    price_expires_date: datetime
    product_marketing_point_array: List[MarketingPoint]
    product_keyword_array: List
    product_brand: str

    export: 

    product_category_a

class ProductData(ProductDataBase):
    pass

class ProductDataPart(ProductDataBase):
    pass

class Inventory:
    pass

class MediaContent:
    pass

class PPC:
    pass






# get the sub-objects that are inside of arrays