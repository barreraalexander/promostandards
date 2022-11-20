import xmltodict

class PPCOperations:
    @staticmethod
    def getAvailableLocations(xml_dict):

        response_dict = {'AvailableLocation': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'locationName': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'locationName1'}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml

    @staticmethod
    def getDecorationColors(xml_dict):

        response_dict = {'GetDecorationColorsRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'decorationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'l1'}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml

    @staticmethod
    def getFobPoints(xml_dict):

        response_dict = {'FobPoint': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'fobId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'fobCity': 'fobCity1', 'fobState': 'fobState1', 'fobPostalCode': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'fobPostalCode1'}, 'fobCountry': 'fobCountry1', 'CurrencySupportedArray': {'CurrencySupported': [{'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'AFA'}}, {'currency': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'ALL'}}]}, 'ProductArray': {'Product': [{'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}}, {'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token2'}}]}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml


    @staticmethod
    def getAvailableCharges(xml_dict):
        response_dict = {'AvailableCharge': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'chargeId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'chargeName': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'chargeDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'chargeType': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Order'}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml


    @staticmethod
    def getConfigurationAndPricing(xml_dict):
        response_dict = {'Part': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/', 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'partDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'PartPriceArray': {'PartPrice': [{'minQuantity': '1', 'price': '1', 'discountCode': '1', 'priceUom': 'BX', 'priceEffectiveDate': {'@xsi:nil': 'true'}, 'priceExpiryDate': {'@xsi:nil': 'true'}}, {'minQuantity': '-2147483647', 'price': '-79228162514264337593543950335', 'discountCode': '2', 'priceUom': 'CA', 'priceEffectiveDate': '1900-01-01T01:01:01.0000000+00:00', 'priceExpiryDate': '1900-01-01T01:01:01.0000000+00:00'}]}, 'partGroup': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'nextPartGroup': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'partGroupRequired': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'true'}, 'partGroupDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': 'Token1'}, 'ratio': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}, 'defaultPart': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'LocationIdArray': {'LocationId': [{'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '1'}}, {'locationId': {'@xmlns': 'http://www.promostandards.org/WSDL/PricingAndConfiguration/1.0.0/SharedObjects/', '#text': '-2147483647'}}]}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml