from pydantic import BaseModel, validator, ValidationError
from typing import Optional, List
from datetime import datetime


class UserOut(BaseModel):
    id: int
    username: str
    # class Config:
    #     orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[str]

class AvailableCharge(BaseModel):
    charge_id: int
    charge_name: str
    charge_type: str
    charge_description: str

class ChargePrice(BaseModel):
    x_min_qty: int
    x_uom: str
    y_min_qty: int
    y_uom: str
    price: float
    discount_code: Optional[str]
    repeat_price: Optional[float]
    repeat_discount_code: Optional[str]
    price_effective_date: Optional[datetime]
    price_expiry_date: Optional[datetime]


class Charge(AvailableCharge):
    charge_price_array: List[ChargePrice]
    charge_applies_ltm: bool
    charges_per_location: Optional[int]
    charges_per_color: Optional[int]
    
class PPC_Color(BaseModel):
    color_id: int
    color_name: str

# class PPC_Color(BaseModel):
#     color_id: str
#     color_name: str

class DecorationMethod(BaseModel):
    decoration_id: int
    decoration_name: str

class DecorationColor(BaseModel):
    color_array: List[PPC_Color]
    product_id: str
    location_id: str
    decoration_method_array: List[DecorationMethod]
    # deocoration_method_array: List[DecorationMethod]
    pms_match: bool
    full_color: bool

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

class AvailableLocation(Location):
    pass 


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
    # description: Optional[str]
    description: List[str]
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

class Currency(BaseModel):
    currency: str


class PPC_Product(BaseModel):
    product_id: str


class PPC_FobPoint(FobPoint):
    currency_supported_array: List[Currency]
    product_array: List[PPC_Product]


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


class ServiceMessage(BaseModel):
    code: int
    description: str
    severity: str

class Quantity(BaseModel):
    uom: str

class FutureAvailability(BaseModel):
    quantity: Quantity
    available_on: datetime

class Filter(BaseModel):
    part_id_array: Optional[List[str]]
    label_size_array: Optional[List[str]]
    part_color_array: Optional[List[str]]


class InventoryLocation(BaseModel):
    inventory_location_id: str
    inventory_location_name: Optional[str]
    postal_code: str
    country: str
    inventory_location_quantity: Quantity
    future_availability_array: List[FutureAvailability]



class PartInventory(BaseModel):
    part_id: str
    main_part: bool
    part_color: Optional[str]
    label_size: Optional[str]
    part_description: Optional[str]
    quantity_available: Optional[Quantity]
    manufactured_item: bool
    buy_to_order: bool
    replenishment_lead_time: Optional[int]
    attribute_selection: Optional[str]
    inventory_location_array: List[InventoryLocation]
    last_modified: Optional[datetime]

# This object contains pricing a product based on the partId.
# Prices are additive in nature. A configuration that requires
# three parts with three different prices should be summed
# together on the purchase order.
class PartPrice(BaseModel):
    min_quantity: int
    price: float
    discount_code: Optional[str]
    price_uom: str
    price_effective_date = datetime
    price_expiry_date = datetime

class PPC_Part(BaseModel):
    part_id: str
    part_description: Optional[str]
    part_price_array: Optional[List[PartPrice]]
    part_group: int
    next_part_group: Optional[int]
    part_group_required: bool
    part_group_description: str
    # Describes how the amount of partIds that need to be added
    # to the order based on the number of products ordered.
    # Example: If 8 partIds would be required per 1 product ordered,
    # then 8 should be used as the ratio.  If one partId is required
    # for every 8 products, than use .125
    ratio: float
    default_part: Optional[bool]
    location_id_array: List[str]


class Configuration(BaseModel):
    part_array: List[PPC_Part]
    location_array: List[Location]
    product_id: str
    currency: str
    fob_array: List[FobPoint]
    fob_postal_code: Optional[str]
    price_type: str


# This object contains decoration information that are valid for a specific location
class PPC_Decoration(BaseModel):
    decoration_id: int
    decoration_name: Optional[str]
    decoration_geometry: str
    decoration_height: Optional[float]
    decoration_width: Optional[float]
    decoration_diameter: Optional[float]
    decoration_uom: str
    allow_sub_for_default_loaction: bool
    allow_sub_for_default_method: bool
    item_part_quantity_ltm: Optional[int]
    charge_array: Optional[List[Charge]]
    decoration_units_included: Optional[int]
    decoration_units_included_uom: Optional[int]
    decoration_units_max: Optional[int]
    default_decoration: bool
    lead_time: Optional[int]
    rush_lead_time: Optional[int]


# This object contains decoration and location details for a given part.
class PPC_Location(BaseModel):
    location_id: int
    location_name: str
    decoration_array: List[PPC_Decoration]
    decorations_included: int
    default_location: bool
    max_decoration: int
    min_decoration: int
    location_rank: Optional[int]




class ProductDataBase(BaseModel):
    product_id: str
    product_name: str
    location_decoration_array: List[LocationDecoration]
    description: List[str]
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


class ProductSellable(BaseModel):
    product_id: str
    part_id: Optional[str]
    culture_point: Optional[str]
    

class ProductData_getProductRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    localization_country: str
    localization_language: str
    product_id: str
    part_id: Optional[str]
    color_name: str
    apparel_size_array: List[ApparelSize]

class ProductData_getProductDateModifiedRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    culture_name: Optional[str]
    change_time_stamp: Optional[datetime]

# this function will provide a list of Product Ids and optional Part Ids for all items which currently have an isCloseOut value of TRUE.
class ProductData_getProductCloseOutRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]

# This function will provide a list of Product Ids and optional Part Ids along with their status of available to sell (Sellable TRUE or FALSE).
class ProductData_getProductSellableRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    localization_country: str
    localization_language: str
    product_id: str
    part_id: Optional[str]
    line_name: Optional[str]
    is_sellable: bool



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


class Inventory:
    pass



class PPCBase(BaseModel):
    ws_version: Optional[str]
    id: str
    password: Optional[str]
    product_id: str
    localization_country: str
    localization_language: str


class PPC(PPCBase):
    class Config:
        orm_mode = True

class PPC_getAvailableLocationsRequest(PPC):
    pass

class PPC_getAvailableLocationsResponse(PPC):    
    available_location_array: List[Location]

class PPC_getDecorationColorsRequest(PPC):
    product_id: Optional[str]
    location_id: Optional[str]
    decoration_id: Optional[int]

    
class PPC_getDecorationColorsResponse():
    decoration_colors: List[Color]



class PPC_getFobPointsRequest(PPC):
    product_id: Optional[str]
    localization_country: str
    localization_language: str

class PPC_getFobPointsResponse(PPC):
    fob_point_array: List[FobPoint]


class PPC_getAvailableChargesRequest(PPC):
    pass


class PPC_getAvailableChargesResponse(PPC):
    available_charge_array: List[AvailableCharge]



class PPC_getConfigurationAndPricingRequest(PPC):
    part_id: Optional[str]
    currency: str
    fob_id: str
    price_type: str
    configuration_type: str


class PPC_getConfigurationAndPricingResponse(PPC):
    available_charge_array: List[AvailableCharge]





class Inventory_getInventoryLevelsRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    product_id: str
    filter: Filter

class Inventory_getFilterValuesRequest(BaseModel):
    ws_version: str
    id: str
    password: Optional[str]
    product_id: str
