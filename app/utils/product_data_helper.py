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
        # do stuff with the request you received
        print (xml_dict)

        # create a response dict
        response_dict = {'Product': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'productName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'priceExpiresDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductMarketingPointArray': {'ProductMarketingPoint': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token1', 'pointCopy': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token2', 'pointCopy': 'Token2'}]}, 'ProductKeywordArray': {'ProductKeyword': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token2'}]}, 'productBrand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'export': {'@xsi:nil': 'true'}, 'ProductCategoryArray': {'ProductCategory': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token1', 'subCategory': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token2', 'subCategory': 'Token2'}]}, 'RelatedProductArray': {'RelatedProduct': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Substitute', 'productId': 'Token1', 'partId': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Companion Sell', 'productId': 'Token2', 'partId': 'Token2'}]}, 'primaryImageUrl': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ProductPriceGroupArray': {'ProductPriceGroup': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '1', 'quantityMax': '1', 'price': '1', 'discountCode': 'Toke1'}, {'quantityMin': '-2147483647', 'quantityMax': '-2147483647', 'price': '-79228162514264337593543950335', 'discountCode': 'Toke2'}]}, 'groupName': 'Token1', 'currency': 'AFA', 'description': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '2147483647', 'quantityMax': '2147483647', 'price': '79228162514264337593543950335', 'discountCode': 'Toke3'}, {'quantityMin': '0', 'quantityMax': '0', 'price': '0.9', 'discountCode': 'Toke4'}]}, 'groupName': 'Token2', 'currency': 'ALL', 'description': 'Token2'}]}, 'complianceInfoAvailable': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'unspscCommodityCode': '1', 'LocationDecorationArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'LocationDecoration': [{'locationName': 'Token1', 'maxImprintColors': '1', 'decorationName': 'Token1', 'locationDecorationComboDefault': 'true', 'priceIncludes': 'true'}, {'locationName': 'Token2', 'maxImprintColors': '-2147483647', 'decorationName': 'Token2', 'locationDecorationComboDefault': 'false', 'priceIncludes': 'false'}]}, 'ProductPartArray': {'ProductPart': [{'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token1', 'hex': 'Token1', 'approximatePms': 'Token1', 'colorName': 'Token1'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AF'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Length', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Thickness', 'SpecificationUom': 'Token1', 'measurementValue': 'Token2'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, 'leadTime': '1', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}}, {'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token2', 'hex': 'Token2', 'approximatePms': 'Token2', 'colorName': 'Token2'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token4'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AX'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Radius', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Volume', 'SpecificationUom': 'Token2', 'measurementValue': 'Token4'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}, 'leadTime': '-2147483647', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '-79228162514264337593543950335'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}}]}, 'lastChangeDate': '1900-01-01T01:01:01.0000000+00:00', 'creationDate': '1900-01-01T01:01:01.0000000+00:00', 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'lineName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultSetupCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultRunCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'imprintSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'FobPointArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'FobPoint': [{'fobId': 'Token1', 'fobCity': 'fobCity1', 'fobState': 'fobState1', 'fobPostalCode': 'fobPostalCode1', 'fobCountry': 'fobCountry1'}, {'fobId': 'Token2', 'fobCity': 'fobCity2', 'fobState': 'fobState2', 'fobPostalCode': 'fobPostalCode2', 'fobCountry': 'fobCountry2'}]}}}

        # convert response dict to xml
        response_xml = xmltodict.unparse(response_dict)

        return response_xml

    
    @staticmethod
    def getProductCloseOutRequest(xml_dict):
        # do stuff with the request you received
        print (xml_dict)

        # create a response dict
        response_dict = {'Product': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'productName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'priceExpiresDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductMarketingPointArray': {'ProductMarketingPoint': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token1', 'pointCopy': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token2', 'pointCopy': 'Token2'}]}, 'ProductKeywordArray': {'ProductKeyword': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token2'}]}, 'productBrand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'export': {'@xsi:nil': 'true'}, 'ProductCategoryArray': {'ProductCategory': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token1', 'subCategory': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token2', 'subCategory': 'Token2'}]}, 'RelatedProductArray': {'RelatedProduct': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Substitute', 'productId': 'Token1', 'partId': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Companion Sell', 'productId': 'Token2', 'partId': 'Token2'}]}, 'primaryImageUrl': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ProductPriceGroupArray': {'ProductPriceGroup': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '1', 'quantityMax': '1', 'price': '1', 'discountCode': 'Toke1'}, {'quantityMin': '-2147483647', 'quantityMax': '-2147483647', 'price': '-79228162514264337593543950335', 'discountCode': 'Toke2'}]}, 'groupName': 'Token1', 'currency': 'AFA', 'description': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '2147483647', 'quantityMax': '2147483647', 'price': '79228162514264337593543950335', 'discountCode': 'Toke3'}, {'quantityMin': '0', 'quantityMax': '0', 'price': '0.9', 'discountCode': 'Toke4'}]}, 'groupName': 'Token2', 'currency': 'ALL', 'description': 'Token2'}]}, 'complianceInfoAvailable': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'unspscCommodityCode': '1', 'LocationDecorationArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'LocationDecoration': [{'locationName': 'Token1', 'maxImprintColors': '1', 'decorationName': 'Token1', 'locationDecorationComboDefault': 'true', 'priceIncludes': 'true'}, {'locationName': 'Token2', 'maxImprintColors': '-2147483647', 'decorationName': 'Token2', 'locationDecorationComboDefault': 'false', 'priceIncludes': 'false'}]}, 'ProductPartArray': {'ProductPart': [{'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token1', 'hex': 'Token1', 'approximatePms': 'Token1', 'colorName': 'Token1'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AF'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Length', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Thickness', 'SpecificationUom': 'Token1', 'measurementValue': 'Token2'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, 'leadTime': '1', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}}, {'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token2', 'hex': 'Token2', 'approximatePms': 'Token2', 'colorName': 'Token2'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token4'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AX'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Radius', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Volume', 'SpecificationUom': 'Token2', 'measurementValue': 'Token4'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}, 'leadTime': '-2147483647', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '-79228162514264337593543950335'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}}]}, 'lastChangeDate': '1900-01-01T01:01:01.0000000+00:00', 'creationDate': '1900-01-01T01:01:01.0000000+00:00', 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'lineName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultSetupCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultRunCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'imprintSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'FobPointArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'FobPoint': [{'fobId': 'Token1', 'fobCity': 'fobCity1', 'fobState': 'fobState1', 'fobPostalCode': 'fobPostalCode1', 'fobCountry': 'fobCountry1'}, {'fobId': 'Token2', 'fobCity': 'fobCity2', 'fobState': 'fobState2', 'fobPostalCode': 'fobPostalCode2', 'fobCountry': 'fobCountry2'}]}}}

        # convert response dict to xml
        response_xml = xmltodict.unparse(response_dict)

        return response_xml
    
    @staticmethod
    def getProductSellableRequest(xml_dict):
        # do stuff with the request you received
        print (xml_dict)

        # create a response dict
        response_dict = {'Product': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'productName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'priceExpiresDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductMarketingPointArray': {'ProductMarketingPoint': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token1', 'pointCopy': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'pointType': 'Token2', 'pointCopy': 'Token2'}]}, 'ProductKeywordArray': {'ProductKeyword': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'keyword': 'Token2'}]}, 'productBrand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'export': {'@xsi:nil': 'true'}, 'ProductCategoryArray': {'ProductCategory': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token1', 'subCategory': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'category': 'Token2', 'subCategory': 'Token2'}]}, 'RelatedProductArray': {'RelatedProduct': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Substitute', 'productId': 'Token1', 'partId': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'relationType': 'Companion Sell', 'productId': 'Token2', 'partId': 'Token2'}]}, 'primaryImageUrl': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ProductPriceGroupArray': {'ProductPriceGroup': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '1', 'quantityMax': '1', 'price': '1', 'discountCode': 'Toke1'}, {'quantityMin': '-2147483647', 'quantityMax': '-2147483647', 'price': '-79228162514264337593543950335', 'discountCode': 'Toke2'}]}, 'groupName': 'Token1', 'currency': 'AFA', 'description': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ProductPriceArray': {'ProductPrice': [{'quantityMin': '2147483647', 'quantityMax': '2147483647', 'price': '79228162514264337593543950335', 'discountCode': 'Toke3'}, {'quantityMin': '0', 'quantityMax': '0', 'price': '0.9', 'discountCode': 'Toke4'}]}, 'groupName': 'Token2', 'currency': 'ALL', 'description': 'Token2'}]}, 'complianceInfoAvailable': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'unspscCommodityCode': '1', 'LocationDecorationArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'LocationDecoration': [{'locationName': 'Token1', 'maxImprintColors': '1', 'decorationName': 'Token1', 'locationDecorationComboDefault': 'true', 'priceIncludes': 'true'}, {'locationName': 'Token2', 'maxImprintColors': '-2147483647', 'decorationName': 'Token2', 'locationDecorationComboDefault': 'false', 'priceIncludes': 'false'}]}, 'ProductPartArray': {'ProductPart': [{'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token1', 'hex': 'Token1', 'approximatePms': 'Token1', 'colorName': 'Token1'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AF'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Length', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token1'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Thickness', 'SpecificationUom': 'Token1', 'measurementValue': 'Token2'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, 'leadTime': '1', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token1', 'description': 'Token1', 'quantity': '1', 'dimensionUom': 'MM', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'ME', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token2', 'description': 'Token2', 'quantity': '-79228162514264337593543950335', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}}, {'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'primaryColor': {'Color': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'standardColorName': 'Token2', 'hex': 'Token2', 'approximatePms': 'Token2', 'colorName': 'Token2'}}, 'description': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token4'}], 'countryOfOrigin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'AX'}, 'ColorArray': {'Color': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'}]}, 'primaryMaterial': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'SpecificationArray': {'Specification': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Radius', 'SpecificationUom': {'@xsi:nil': 'true'}, 'measurementValue': 'Token3'}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'specificationType': 'Volume', 'SpecificationUom': 'Token2', 'measurementValue': 'Token4'}]}, 'shape': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'ApparelSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}, 'Dimension': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'dimensionUom': 'CM', 'depth': '1', 'height': '1', 'width': '1', 'weightUom': 'KG', 'weight': '1'}, 'leadTime': '-2147483647', 'unspsc': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'gtin': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isRushService': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'ProductPackagingArray': {'ProductPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'true', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'default': 'false', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'ShippingPackageArray': {'ShippingPackage': [{'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token3', 'description': 'Token3', 'quantity': '79228162514264337593543950335', 'dimensionUom': 'MR', 'depth': {'@xsi:nil': 'true'}, 'height': {'@xsi:nil': 'true'}, 'width': {'@xsi:nil': 'true'}, 'weightUom': 'OZ', 'weight': {'@xsi:nil': 'true'}}, {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'packageType': 'Token4', 'description': 'Token4', 'quantity': '0.9', 'dimensionUom': 'IN', 'depth': '-79228162514264337593543950335', 'height': '-79228162514264337593543950335', 'width': '-79228162514264337593543950335', 'weightUom': 'LB', 'weight': '-79228162514264337593543950335'}]}, 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '1900-01-01T01:01:01.0000000+00:00'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcCode': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': '-79228162514264337593543950335'}, 'nmfcDescription': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'nmfcNumber': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token2'}, 'isOnDemand': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}, 'isHazmat': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'true'}}]}, 'lastChangeDate': '1900-01-01T01:01:01.0000000+00:00', 'creationDate': '1900-01-01T01:01:01.0000000+00:00', 'endDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'effectiveDate': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'isCaution': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'cautionComment': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'isCloseout': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '@xsi:nil': 'true'}, 'lineName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultSetupCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'defaultRunCharge': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'imprintSize': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'FobPointArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'FobPoint': [{'fobId': 'Token1', 'fobCity': 'fobCity1', 'fobState': 'fobState1', 'fobPostalCode': 'fobPostalCode1', 'fobCountry': 'fobCountry1'}, {'fobId': 'Token2', 'fobCity': 'fobCity2', 'fobState': 'fobState2', 'fobPostalCode': 'fobPostalCode2', 'fobCountry': 'fobCountry2'}]}}}

        # convert response dict to xml
        response_xml = xmltodict.unparse(response_dict)

        return response_xml

    















    # print (request)
    # print (dir(request))

    # print (request.method)
    # request_xml = request.data




    # # print (request_xml)
    # # xml_dict = xmltodict.parse(request_xml)
    # # print (xml_dict)


    # # custom_dict = {
    # #     'env:Envelope' : {
    # #         '@xmlns:env' : 'http://schemas.xmlsoap.org/soap/envelope/'

    # #     }
    # # }

    # mock_product = {
        
    # }


    # custom_dict = {
    #     'env:Envelope': {
    #         '@xmlns:env': 'http://schemas.xmlsoap.org/soap/envelope/',
    #         'env:Body': {
    #             'GetRelevanceResult': {
    #                 '@xmlns': 'http://[webreportshostname]:[webreportsport]      /webreports?wsdl',
    #                 'relevanceExpr': 'names of bes computers', 'username': 'user', 'password': 'password'
    #                 }
    #             }
    #         }
    #     }

    # custom_xml = xmltodict.unparse()

    # print (custom_xml)

    # return jsonify({'root' : 'root'})


# example of getProductRequest turn to dictionary

# {'GetProductRequest': {'@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', '@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/', 'wsVersion': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'id': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'password': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'localizationCountry': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'localizationLanguage': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'T1'}, 'productId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'partId': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'colorName': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', '#text': 'Token1'}, 'ApparelSizeArray': {'@xmlns': 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/', 'ApparelSize': [{'apparelStyle': 'Unisex', 'labelSize': 'OSFA', 'customSize': 'Token1'}, {'apparelStyle': 'Youth', 'labelSize': '6XS', 'customSize': 'Token2'}]}}}














# example of product response (converted to dict)











# example of product response (raw xml)



# <Product xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/">
# <productId xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</productId>
# <productName xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</productName>
# <description xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</description>
# <description xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</description>
# <priceExpiresDate xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <ProductMarketingPointArray>
# <ProductMarketingPoint xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <pointType>Token1</pointType>
# <pointCopy>Token1</pointCopy>
# </ProductMarketingPoint>
# <ProductMarketingPoint xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <pointType>Token2</pointType>
# <pointCopy>Token2</pointCopy>
# </ProductMarketingPoint>
# </ProductMarketingPointArray>
# <ProductKeywordArray>
# <ProductKeyword xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <keyword>Token1</keyword>
# </ProductKeyword>
# <ProductKeyword xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <keyword>Token2</keyword>
# </ProductKeyword>
# </ProductKeywordArray>
# <productBrand xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</productBrand>
# <export xsi:nil="true"/>
# <ProductCategoryArray>
# <ProductCategory xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <category>Token1</category>
# <subCategory>Token1</subCategory>
# </ProductCategory>
# <ProductCategory xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <category>Token2</category>
# <subCategory>Token2</subCategory>
# </ProductCategory>
# </ProductCategoryArray>
# <RelatedProductArray>
# <RelatedProduct xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <relationType>Substitute</relationType>
# <productId>Token1</productId>
# <partId>Token1</partId>
# </RelatedProduct>
# <RelatedProduct xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <relationType>Companion Sell</relationType>
# <productId>Token2</productId>
# <partId>Token2</partId>
# </RelatedProduct>
# </RelatedProductArray>
# <primaryImageUrl xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</primaryImageUrl>
# <ProductPriceGroupArray>
# <ProductPriceGroup xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <ProductPriceArray>
# <ProductPrice>
# <quantityMin>1</quantityMin>
# <quantityMax>1</quantityMax>
# <price>1</price>
# <discountCode>Toke1</discountCode>
# </ProductPrice>
# <ProductPrice>
# <quantityMin>-2147483647</quantityMin>
# <quantityMax>-2147483647</quantityMax>
# <price>-79228162514264337593543950335</price>
# <discountCode>Toke2</discountCode>
# </ProductPrice>
# </ProductPriceArray>
# <groupName>Token1</groupName>
# <currency>AFA</currency>
# <description>Token1</description>
# </ProductPriceGroup>
# <ProductPriceGroup xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <ProductPriceArray>
# <ProductPrice>
# <quantityMin>2147483647</quantityMin>
# <quantityMax>2147483647</quantityMax>
# <price>79228162514264337593543950335</price>
# <discountCode>Toke3</discountCode>
# </ProductPrice>
# <ProductPrice>
# <quantityMin>0</quantityMin>
# <quantityMax>0</quantityMax>
# <price>0.9</price>
# <discountCode>Toke4</discountCode>
# </ProductPrice>
# </ProductPriceArray>
# <groupName>Token2</groupName>
# <currency>ALL</currency>
# <description>Token2</description>
# </ProductPriceGroup>
# </ProductPriceGroupArray>
# <complianceInfoAvailable xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <unspscCommodityCode>1</unspscCommodityCode>
# <LocationDecorationArray xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <LocationDecoration>
# <locationName>Token1</locationName>
# <maxImprintColors>1</maxImprintColors>
# <decorationName>Token1</decorationName>
# <locationDecorationComboDefault>true</locationDecorationComboDefault>
# <priceIncludes>true</priceIncludes>
# </LocationDecoration>
# <LocationDecoration>
# <locationName>Token2</locationName>
# <maxImprintColors>-2147483647</maxImprintColors>
# <decorationName>Token2</decorationName>
# <locationDecorationComboDefault>false</locationDecorationComboDefault>
# <priceIncludes>false</priceIncludes>
# </LocationDecoration>
# </LocationDecorationArray>
# <ProductPartArray>
# <ProductPart>
# <partId xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</partId>
# <primaryColor>
# <Color xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <standardColorName>Token1</standardColorName>
# <hex>Token1</hex>
# <approximatePms>Token1</approximatePms>
# <colorName>Token1</colorName>
# </Color>
# </primaryColor>
# <description xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</description>
# <description xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</description>
# <countryOfOrigin xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">AF</countryOfOrigin>
# <ColorArray>
# <Color xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/"/>
# <Color xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/"/>
# </ColorArray>
# <primaryMaterial xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</primaryMaterial>
# <SpecificationArray>
# <Specification xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <specificationType>Length</specificationType>
# <SpecificationUom xsi:nil="true"/>
# <measurementValue>Token1</measurementValue>
# </Specification>
# <Specification xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <specificationType>Thickness</specificationType>
# <SpecificationUom>Token1</SpecificationUom>
# <measurementValue>Token2</measurementValue>
# </Specification>
# </SpecificationArray>
# <shape xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</shape>
# <ApparelSize xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <apparelStyle>Unisex</apparelStyle>
# <labelSize>OSFA</labelSize>
# <customSize>Token1</customSize>
# </ApparelSize>
# <Dimension xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <dimensionUom>MM</dimensionUom>
# <depth xsi:nil="true"/>
# <height xsi:nil="true"/>
# <width xsi:nil="true"/>
# <weightUom>ME</weightUom>
# <weight xsi:nil="true"/>
# </Dimension>
# <leadTime>1</leadTime>
# <unspsc xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</unspsc>
# <gtin xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</gtin>
# <isRushService xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <ProductPackagingArray>
# <ProductPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <default>true</default>
# <packageType>Token1</packageType>
# <description>Token1</description>
# <quantity>1</quantity>
# <dimensionUom>MM</dimensionUom>
# <depth xsi:nil="true"/>
# <height xsi:nil="true"/>
# <width xsi:nil="true"/>
# <weightUom>ME</weightUom>
# <weight xsi:nil="true"/>
# </ProductPackage>
# <ProductPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <default>false</default>
# <packageType>Token2</packageType>
# <description>Token2</description>
# <quantity>-79228162514264337593543950335</quantity>
# <dimensionUom>CM</dimensionUom>
# <depth>1</depth>
# <height>1</height>
# <width>1</width>
# <weightUom>KG</weightUom>
# <weight>1</weight>
# </ProductPackage>
# </ProductPackagingArray>
# <ShippingPackageArray>
# <ShippingPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <packageType>Token1</packageType>
# <description>Token1</description>
# <quantity>1</quantity>
# <dimensionUom>MM</dimensionUom>
# <depth xsi:nil="true"/>
# <height xsi:nil="true"/>
# <width xsi:nil="true"/>
# <weightUom>ME</weightUom>
# <weight xsi:nil="true"/>
# </ShippingPackage>
# <ShippingPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <packageType>Token2</packageType>
# <description>Token2</description>
# <quantity>-79228162514264337593543950335</quantity>
# <dimensionUom>CM</dimensionUom>
# <depth>1</depth>
# <height>1</height>
# <width>1</width>
# <weightUom>KG</weightUom>
# <weight>1</weight>
# </ShippingPackage>
# </ShippingPackageArray>
# <endDate xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <effectiveDate xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <isCloseout xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <isCaution xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <cautionComment xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</cautionComment>
# <nmfcCode xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">1</nmfcCode>
# <nmfcDescription xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</nmfcDescription>
# <nmfcNumber xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</nmfcNumber>
# <isOnDemand xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <isHazmat xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# </ProductPart>
# <ProductPart>
# <partId xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</partId>
# <primaryColor>
# <Color xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <standardColorName>Token2</standardColorName>
# <hex>Token2</hex>
# <approximatePms>Token2</approximatePms>
# <colorName>Token2</colorName>
# </Color>
# </primaryColor>
# <description xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token3</description>
# <description xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token4</description>
# <countryOfOrigin xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">AX</countryOfOrigin>
# <ColorArray>
# <Color xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/"/>
# <Color xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/"/>
# </ColorArray>
# <primaryMaterial xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</primaryMaterial>
# <SpecificationArray>
# <Specification xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <specificationType>Radius</specificationType>
# <SpecificationUom xsi:nil="true"/>
# <measurementValue>Token3</measurementValue>
# </Specification>
# <Specification xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <specificationType>Volume</specificationType>
# <SpecificationUom>Token2</SpecificationUom>
# <measurementValue>Token4</measurementValue>
# </Specification>
# </SpecificationArray>
# <shape xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</shape>
# <ApparelSize xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <apparelStyle>Youth</apparelStyle>
# <labelSize>6XS</labelSize>
# <customSize>Token2</customSize>
# </ApparelSize>
# <Dimension xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <dimensionUom>CM</dimensionUom>
# <depth>1</depth>
# <height>1</height>
# <width>1</width>
# <weightUom>KG</weightUom>
# <weight>1</weight>
# </Dimension>
# <leadTime>-2147483647</leadTime>
# <unspsc xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</unspsc>
# <gtin xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</gtin>
# <isRushService xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">true</isRushService>
# <ProductPackagingArray>
# <ProductPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <default>true</default>
# <packageType>Token3</packageType>
# <description>Token3</description>
# <quantity>79228162514264337593543950335</quantity>
# <dimensionUom>MR</dimensionUom>
# <depth xsi:nil="true"/>
# <height xsi:nil="true"/>
# <width xsi:nil="true"/>
# <weightUom>OZ</weightUom>
# <weight xsi:nil="true"/>
# </ProductPackage>
# <ProductPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <default>false</default>
# <packageType>Token4</packageType>
# <description>Token4</description>
# <quantity>0.9</quantity>
# <dimensionUom>IN</dimensionUom>
# <depth>-79228162514264337593543950335</depth>
# <height>-79228162514264337593543950335</height>
# <width>-79228162514264337593543950335</width>
# <weightUom>LB</weightUom>
# <weight>-79228162514264337593543950335</weight>
# </ProductPackage>
# </ProductPackagingArray>
# <ShippingPackageArray>
# <ShippingPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <packageType>Token3</packageType>
# <description>Token3</description>
# <quantity>79228162514264337593543950335</quantity>
# <dimensionUom>MR</dimensionUom>
# <depth xsi:nil="true"/>
# <height xsi:nil="true"/>
# <width xsi:nil="true"/>
# <weightUom>OZ</weightUom>
# <weight xsi:nil="true"/>
# </ShippingPackage>
# <ShippingPackage xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <packageType>Token4</packageType>
# <description>Token4</description>
# <quantity>0.9</quantity>
# <dimensionUom>IN</dimensionUom>
# <depth>-79228162514264337593543950335</depth>
# <height>-79228162514264337593543950335</height>
# <width>-79228162514264337593543950335</width>
# <weightUom>LB</weightUom>
# <weight>-79228162514264337593543950335</weight>
# </ShippingPackage>
# </ShippingPackageArray>
# <endDate xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">1900-01-01T01:01:01.0000000+00:00</endDate>
# <effectiveDate xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">1900-01-01T01:01:01.0000000+00:00</effectiveDate>
# <isCloseout xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">true</isCloseout>
# <isCaution xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">true</isCaution>
# <cautionComment xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</cautionComment>
# <nmfcCode xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">-79228162514264337593543950335</nmfcCode>
# <nmfcDescription xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</nmfcDescription>
# <nmfcNumber xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token2</nmfcNumber>
# <isOnDemand xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">true</isOnDemand>
# <isHazmat xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">true</isHazmat>
# </ProductPart>
# </ProductPartArray>
# <lastChangeDate>1900-01-01T01:01:01.0000000+00:00</lastChangeDate>
# <creationDate>1900-01-01T01:01:01.0000000+00:00</creationDate>
# <endDate xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <effectiveDate xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <isCaution xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <cautionComment xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</cautionComment>
# <isCloseout xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/" xsi:nil="true"/>
# <lineName xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</lineName>
# <defaultSetupCharge xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</defaultSetupCharge>
# <defaultRunCharge xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</defaultRunCharge>
# <imprintSize xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">Token1</imprintSize>
# <FobPointArray xmlns="http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/">
# <FobPoint>
# <fobId>Token1</fobId>
# <fobCity>fobCity1</fobCity>
# <fobState>fobState1</fobState>
# <fobPostalCode>fobPostalCode1</fobPostalCode>
# <fobCountry>fobCountry1</fobCountry>
# </FobPoint>
# <FobPoint>
# <fobId>Token2</fobId>
# <fobCity>fobCity2</fobCity>
# <fobState>fobState2</fobState>
# <fobPostalCode>fobPostalCode2</fobPostalCode>
# <fobCountry>fobCountry2</fobCountry>
# </FobPoint>
# </FobPointArray>
# </Product>



