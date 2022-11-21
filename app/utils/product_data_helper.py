import xmltodict

class ProductDataOperations:
    @staticmethod
    def getProductRequest(xml_dict):
        # do stuff with the request you received
        print (xml_dict)

        # create a response dict
        response_dict = {'Product': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'productName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'priceExpiresDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductMarketingPointArray': {'ProductMarketingPoint': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token1', 'pointCopy': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token2', 'pointCopy': 'Token2'}]}, 'ProductKeywordArray': {'ProductKeyword': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token2'}]}, 'productBrand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'export': {'@xsi:nil': 'true'}, 'ProductCategoryArray': {'ProductCategory': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token1', 'subCategory': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token2', 'subCategory': 'Token2'}]}, 'RelatedProductArray': {'RelatedProduct': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Substitute', 'productId': 'Token1', 'partId': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Companion Sell', 'productId': 'Token2', 'partId': 'Token2'}]}, 'primaryImageUrl': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ProductPriceGroupArray': {'ProductPriceGroup': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '1', 'quantityMax': '1', 'price': '1', 'discountCode': 'Toke1'}, {'quantityMin': '-2147483647', 'quantityMax': '-2147483647', 'price': '-79228162514264337593543950335', 'discountCode': 'Toke2'}]}, 'groupName': 'Token1', 'currency': 'AFA', 'description': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '2147483647', 'quantityMax': '2147483647', 'price': '79228162514264337593543950335', 'discountCode': 'Toke3'}, {'quantityMin': '0', 'quantityMax': '0', 'price': '0.9', 'discountCode': 'Toke4'}]}, 'groupName': 'Token2', 'currency': 'ALL', 'description': 'Token2'}]}, 'complianceInfoAvailable': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'unspscCommodityCode': '1', 'LocationDecorationArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'LocationDecoration': [{'locationName': 'Token1', 'maxImprintColors': '1', 'decorationName': 'Token1', 'locationDecorationComboDefault': 'true', 'priceIncludes': 'true'}, {'locationName': 'Token2', 'maxImprintColors': '-2147483647', 'decorationName': 'Token2', 'locationDecorationComboDefault': 'false', 'priceIncludes': 'false'}]}, 'ProductPartArray': {'ProductPart': [{'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token1', 'hex': 'Token1', 'approximatePms': 'Token1', 'colorName': 'Token1'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AF'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Length', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Thickness', 'SpecificationUom': 'Token1', 'measurementValue': 'Token2'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, 'leadTime': '1', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}}, {'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token2', 'hex': 'Token2', 'approximatePms': 'Token2', 'colorName': 'Token2'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token4'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AX'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Radius', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Volume', 'SpecificationUom': 'Token2', 'measurementValue': 'Token4'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}, 'leadTime': '-2147483647', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '-79228162514264337593543950335'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}}]}, 'lastChangeDate': '1900-01-01T01:01:01.0000000+00:00', 'creationDate': '1900-01-01T01:01:01.0000000+00:00', 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'lineName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultSetupCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultRunCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'imprintSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'FobPointArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'FobPoint': [{'fobId': 'Token1', 'fobCity': 'fobCity1', 'fobState': 'fobState1', 'fobPostalCode': 'fobPostalCode1', 'fobCountry': 'fobCountry1'}, {'fobId': 'Token2', 'fobCity': 'fobCity2', 'fobState': 'fobState2', 'fobPostalCode': 'fobPostalCode2', 'fobCountry': 'fobCountry2'}]}}}

        # convert response dict to xml
        response_xml = xmltodict.unparse(response_dict)

        return response_xml

    
    @staticmethod
    def getProductDateModifiedRequest(xml_dict):

        response_dict = {'ProductDateModified': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml

    
    @staticmethod
    def getProductCloseOutRequest(xml_dict):

        response_dict = {'ProductCloseOut': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}}}   

        response_xml = xmltodict.unparse(response_dict)

        return response_xml
    
    @staticmethod
    def getProductSellableRequest(xml_dict):

        response_dict = {'GetProductSellableResponse': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'ProductSellableArray': {'ProductSellable': [{'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'culturePoint': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}}, {'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'culturePoint': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}}]}, 'ServiceMessageArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ServiceMessage': [{'code': '1', 'description': 'Token1', 'severity': 'Error'}, {'code': '-2147483647', 'description': 'Token2', 'severity': 'Information'}]}}}

        response_xml = xmltodict.unparse(response_dict)

        return response_xml