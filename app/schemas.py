from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Color(BaseModel):
    color_name: str
    hex: Optional[str]
    approximate_pms: Optional[str]
    standard_color_name: Optional[str]

class ClassType(BaseModel):
    class_type: int
    class_name: str

class Specification(BaseModel):
    specification_type: str
    specification_uom: str
    measurement_value: str


class ApparelSize(BaseModel):
    apparel_style: str
    label_size: str
    custom_size: Optional[str]


class Dimension(BaseModel):     
    dimension_uom: str
    depth: Optional[float]
    height: Optional[float]
    width: Optional[float]
    weight_uom: str
    weight: float

class Decoration(BaseModel):
    decoration_id: int
    decoration_name: str

class Location(BaseModel):
    location_id: int
    location_name: str

class LocationDecoration(BaseModel):
    location_name: str
    max_imprint_colors: Optional[int]
    decoration_name: str
    location_decoration_combo_default: bool
    price_includes: bool
        

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
    default: bool
    package_type: str
    description: Optional[str]
    quantity: float
    dimension_uom: str
    depth: Optional[float]
    height: Optional[float]
    width: Optional[float]
    weight_uom: str
    weight: Optional[float]


class ShippingPackaging(BaseModel):
    package_type: str
    description: Optional[str]
    quantity: float
    dimension_uom: str
    depth: Optional[float]
    height: Optional[float]
    width: Optional[float]
    weight_uom: str
    weight: Optional[float]

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

class ProductPrice(BaseModel):
    quantity_max: int
    quantity_min: int
    price: float
    discount_code: Optional[str]

class ProductPriceGroup(BaseModel):
    group_name: str
    currency: str
    description: Optional[str]
    product_price_array: List[ProductPrice]

class ProductDataBase(BaseModel):
    product_id: str
    product_name: str
    location_decoration_array: List[LocationDecoration]
    description: str
    price_expires_date: Optional[datetime]
    product_marketing_point_array: List[ProductMarketingPoint]
    product_keyword_array: List[ProductKeyword]
    product_brand: Optional[str]
    export: bool
    product_category_array: List[ProductCategory]
    related_product_array: List[RelatedProduct]
    product_part_array: List[ProductPart]
    last_change_date: datetime
    creation_date: datetime
    end_date: Optional[datetime]
    effective_date: Optional[datetime]
    is_caution: bool
    caution_comment: Optional[str]
    is_closeout: bool
    line_name: str
    primary_image_url: str
    product_price_group_array: List[ProductPriceGroup]
    compliance_info_available: Optional[bool]
    unspsc_commodity_code: Optional[int]
    imprint_size: Optional[str]
    default_set_up_charge: Optional[str]
    default_run_charge: Optional[str]
    fob_point_array: List[FobPoint]

class ProductData(ProductDataBase):
    class Config:
        orm_mode = True


class MediaContentBase(BaseModel):
    product_id: str
    part_id: Optional[str]
    url: str
    media_type: str
    class_type_array: List[ClassType]
    file_size: Optional[float]
    width: Optional[int]
    height: Optional[int]
    dpi: Optional[int]
    color: Optional[str]
    decoration_array: List[Decoration]
    location_array: List[Location]
    description: Optional[str]
    single_part: bool
    change_time_stamp: Optional[datetime]

class MediaContent(MediaContentBase):
    class Config:
        orm_mode = True

class MediaContent_getMediaContentRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    culture_name: Optional[str]
    media_type: str
    product_id: str
    part_id: Optional[str]
    class_type: int


class MediaContent_getMediaDateModifiedRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    culture_name: Optional[str]
    change_time_stamp: Optional[datetime]


class MediaContent_getMediaDateModifiedResponse(BaseModel):
    product_id: str
    part_id: Optional[str]


class MediaContent_getMediaDateModifiedResponse(MediaContent):
    media_date_modified_array: List[MediaContent]


# class 

    # product_category_a

# class ProductData(ProductDataBase):
#     pass

# class ProductDataPart(ProductDataBase):
#     pass


class Inventory:
    pass


class PPC(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    product_id: str
    localization_country: str
    localization_language: str

class PPC_getAvailableLocationsRequest(PPC):
    available_location_array: List[Location]

class PPC_getDecorationColorRequest():
    decoration_colors: List[Color]


class PPC_getDecorationColorsResponse():
    pass



class PPC_getFobPointsRequest(PPC):
    pass


class PPC_getFobPointsResponse(PPC):
    fob_point_array: List[FobPoint]


class PPC_getAvailableChargesRequest(PPC):
    pass


class PPC_getAvailableChargesResponse(PPC):
    pass
    # fob_point_array: List[A]







# get the sub-objects that are inside of arrays