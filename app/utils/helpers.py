from passlib.context import CryptContext
def unpack_elems(elements):
    return " ".join(elements)


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# COMMON LINKS FOR INVENTORY ITEMS
COMMON_XSI = "http://www.w3.org/2001/XMLSchema-instance"

PPC_COMMON_XMLNS = 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/'
PPC_COMMON_SHARED_OBJECT = 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/'

PRODUCTDATA_COMMON_XMLNS = 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/'
PRODUCTDATA_COMMON_SHARED_OBJECT = 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'

INVENTORY_COMMON_XMLNS = 'http://www.promostandards.org/WSDL/Inventory/2.0.0/'
INVENTORY_COMMON_SHARED_OBJECT = 'http://www.promostandards.org/WSDL/Inventory/2.0.0/SharedObjects/'


MEDIACONTENT_COMMON_XMLNS = 'http://www.promostandards.org/WSDL/MediaService/1.0.0/'
MEDIACONTENT_COMMON_SHARED_OBJECT = 'http://www.promostandards.org/WSDL/MediaService/1.0.0/SharedObjects/'

ENVELOPE_S_XMLNS = "http://schemas.xmlsoap.org/soap/envelope/"
BODY_XSI = "http://www.w3.org/2001/XMLSchema-instance"
BODY_XSD = "http://www.w3.org/2001/XMLSchema"