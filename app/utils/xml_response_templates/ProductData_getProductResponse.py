from lxml import etree
from app import schemas
from typing import List
import json


def xml_response(product_data: schemas.ProductData):
    xsi = 'http://www.w3.org/2001/XMLSchema-instance'
    xmlns = 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/'
    xmlns_shared_objects = 'http://www.promostandards.org/WSDL/ProductDataService/2.0.0/SharedObjects/'


    root = etree.Element('Product', xsi=xsi, xmlns=xmlns)

    ProductId = etree.Element('ProductId', xmlns=xmlns_shared_objects)
    ProductId.text = product_data.product_id
    root.append(ProductId)

    ProductName = etree.Element('ProductName', xmlns=xmlns_shared_objects)
    ProductName.text = product_data.product_name
    root.append(ProductName)

    Description = etree.Element('Description', xmlns=xmlns_shared_objects)
    product_data.description = json.loads(product_data.description)
    if product_data.description:
        for description in product_data.description:
            description_element = etree.Element('description', xmlns=xmlns_shared_objects)
            description_element.text = description
            Description.append(description_element)
    root.append(Description)



    priceExpiresDate = etree.Element('priceExpiresDate', xmlns=xmlns_shared_objects, xsi="true")
    priceExpiresDate.text = str(product_data.price_expires_date)
    root.append(priceExpiresDate)
    # price

    ProductMarketingPointArray = etree.Element('ProductMarketingPointArray')
    product_data.product_marketing_point_array = json.loads(product_data.product_marketing_point_array)
    if product_data.product_marketing_point_array:
        for product_marketing_point in product_data.product_marketing_point_array:
            product_marketing_point_schema = schemas.ProductMarketingPoint(**product_marketing_point)
            ProductMarketingPoint = etree.Element('ProductMarketingPoint')

            pointType = etree.Element('pointType')
            pointType.text = str(product_marketing_point_schema.point_type)
            ProductMarketingPoint.append(pointType)

            pointCopy = etree.Element('pointCopy')
            pointCopy.text = str(product_marketing_point_schema.point_copy)
            ProductMarketingPoint.append(pointCopy)

            ProductMarketingPointArray.append(ProductMarketingPoint)

    root.append(ProductMarketingPointArray)


    ProductKeywordArray = etree.Element('ProductKeywordArray')
    product_data.product_keyword_array = json.loads(product_data.product_keyword_array)
    if product_data.product_keyword_array:
        for product_keyword in product_data.product_keyword_array:
            product_keyword_schema = schemas.ProductKeyword(**product_keyword)
            ProductKeyword = etree.Element('ProductKeyword')

            keyword = etree.Element('keyword')
            keyword.text = product_keyword_schema.keyword
            ProductKeyword.append(keyword)



            ProductKeywordArray.append(ProductKeyword)

    root.append(ProductKeywordArray)

    productBrand = etree.Element('productBrand', xmlns=xmlns_shared_objects)
    productBrand.text = str(product_data.product_brand)
    root.append(productBrand)
    
    export = etree.Element('export', xsi="true")
    export.text = str(product_data.export)
    root.append(export)


    ProductCategoryArray = etree.Element('ProductCategoryArray')
    product_data.product_category_array = json.loads(product_data.product_category_array)
    if product_data.product_category_array:
        for product_category in product_data.product_category_array:
            product_category_schema = schemas.ProductCategory(**product_category)
            ProductCategory = etree.Element('ProductCategory')

            category = etree.Element('category')
            category.text = product_category_schema.category
            ProductCategory.append(category)

            sub_category = etree.Element('subCategory')
            sub_category.text = product_category_schema.sub_category
            ProductCategory.append(sub_category)


            ProductCategoryArray.append(ProductCategory)

    root.append(ProductCategoryArray)

    RelatedProductArray = etree.Element('RelatedProductArray')
    product_data.related_product_array = json.loads(product_data.related_product_array)
    if product_data.related_product_array:
        for related_product in product_data.related_product_array:
            related_product_schema = schemas.RelatedProduct(**related_product)
            RelatedProduct = etree.Element('RelatedProduct', xmlns=xmlns_shared_objects)

            relationType = etree.Element('relationType')
            relationType.text = related_product_schema.relation_type
            RelatedProduct.append(relationType)

            productId = etree.Element('productId')
            productId.text = related_product_schema.product_id
            RelatedProduct.append(productId)

            partId = etree.Element('partId')
            partId.text = related_product_schema.part_id
            RelatedProduct.append(partId)


            RelatedProductArray.append(RelatedProduct)

    root.append(RelatedProductArray)
    
    primaryImageUrl = etree.Element('primaryImageUrl')
    primaryImageUrl.text = str(product_data.primary_image_url)
    root.append(primaryImageUrl)

    ProductPriceGroupArray = etree.Element('ProductPriceGroupArray')
    product_data.product_price_group_array = json.loads(product_data.product_price_group_array)
    if product_data.product_price_group_array:
        for product_price_group in product_data.product_price_group_array:
            product_price_group_schema = schemas.ProductPriceGroup(**product_price_group)
            ProductPriceGroup = etree.Element('ProductPriceGroup', xmlns=xmlns_shared_objects)
            
            for product_price in product_price_group_schema.product_price_array:
                ProductPriceArray = etree.Element('ProductPriceArray')

                ProductPrice = etree.Element('ProductPrice')

                quantityMin = etree.Element('quantityMin')
                quantityMin.text = str(product_price.quantity_min)
                ProductPrice.append(quantityMin)
            
                quantityMax = etree.Element('quantityMax')
                quantityMax.text = str(product_price.quantity_max)
                ProductPrice.append(quantityMax)

                price = etree.Element('price')
                price.text = str(product_price.price)
                ProductPrice.append(price)
            
                discountCode = etree.Element('discountCode')
                discountCode.text = product_price.discount_code
                ProductPrice.append(discountCode)

                ProductPriceArray.append(ProductPrice)

                ProductPriceGroup.append(ProductPriceArray)

            groupName = etree.Element('groupName')
            groupName.text = product_price_group_schema.group_name
            ProductPriceGroup.append(groupName)

            currency = etree.Element('currency')
            currency.text = product_price_group_schema.currency
            ProductPriceGroup.append(currency)

            description = etree.Element('description')
            description.text = product_price_group_schema.description
            ProductPriceGroup.append(description)

            ProductPriceGroupArray.append(ProductPriceGroup)
        
    complianceInfoAvailable = etree.Element('complianceInfoAvailable', xmlns=xmlns_shared_objects, xsi="true")
    complianceInfoAvailable.text = str(product_data.compliance_info_available)
    ProductPriceGroupArray.append(complianceInfoAvailable)

    unspscCommodityCode = etree.Element('unspscCommodityCode')
    unspscCommodityCode.text = str(product_data.unspsc_commodity_code)
    ProductPriceGroupArray.append(unspscCommodityCode)

    root.append(ProductPriceGroupArray)



    LocationDecorationArray = etree.Element('LocationDecorationArray', xmlns=xmlns_shared_objects)
    product_data.location_decoration_array = json.loads(product_data.location_decoration_array)
    if product_data.location_decoration_array:
        for location_decoration in product_data.location_decoration_array:
            location_decoration_schema = schemas.LocationDecoration(**location_decoration)
            LocationDecoration = etree.Element('LocationDecoration')

            locationName = etree.Element('locationName')
            locationName.text = location_decoration_schema.location_name
            LocationDecoration.append(locationName)

            maxImprintColors = etree.Element('maxImprintColors')
            maxImprintColors.text = str(location_decoration_schema.max_imprint_colors)
            LocationDecoration.append(maxImprintColors)

            decorationName = etree.Element('decorationName')
            decorationName.text = location_decoration_schema.decoration_name
            LocationDecoration.append(decorationName)

            locationDecorationComboDefault = etree.Element('locationDecorationComboDefault')
            locationDecorationComboDefault.text = str(location_decoration_schema.location_decoration_combo_default).lower()
            LocationDecoration.append(locationDecorationComboDefault)

            priceIncludes = etree.Element('priceIncludes')
            priceIncludes.text = str(location_decoration_schema.price_includes).lower()
            LocationDecoration.append(priceIncludes)
            
            LocationDecorationArray.append(LocationDecoration)
    root.append(LocationDecorationArray)



    ProductPartArray = etree.Element('ProductPartArray')
    product_data.product_part_array = json.loads(product_data.product_part_array)
    if product_data.product_part_array:
        for product_part in product_data.product_part_array:
            product_part_schema = schemas.ProductPart(**product_part)
            ProductPart = etree.Element('ProductPart')

            partId = etree.Element('partId', xmlns=xmlns_shared_objects)
            partId.text = product_part_schema.part_id
            ProductPart.append(partId)

            primaryColor = etree.Element('primaryColor')
            # primaryColor.text = product_part_schema.primary_color
            ProductPart.append(primaryColor)

            # primaryColor = etree.Element('primaryColor')
            # primaryColor.text = product_part_schema.primary_color
            
            Color = etree.Element('Color', xmlns=xmlns_shared_objects)
            
            standardColorName = etree.Element('standardColorName')
            standardColorName.text = product_part_schema.primary_color.color_name
            Color.append(standardColorName)            

            hex = etree.Element('hex')
            hex.text = product_part_schema.primary_color.hex
            Color.append(hex)            

            approximatePms = etree.Element('approximatePms')
            approximatePms.text = product_part_schema.primary_color.approximate_pms
            Color.append(approximatePms)            

            colorName = etree.Element('colorName')
            colorName.text = product_part_schema.primary_color.color_name
            Color.append(colorName)            

            primaryColor.append(Color)

            ProductPart.append(primaryColor)

            for description in product_part_schema.description:
                description_element = etree.Element('description')
                description_element.text = description
                ProductPart.append(description_element)

             

            countryOfOrigin = etree.Element('countryOfOrigin')
            countryOfOrigin.text = str(product_part_schema.country_of_origin)
            ProductPart.append(countryOfOrigin)


            ColorArray = etree.Element('ColorArray')
            for color in product_part_schema.color_array:
                # Color = etree.Element('Color', xmlns=xmlns_shared_objects)
                # Color.text = color.


                Color = etree.Element('Color', xmlns=xmlns_shared_objects)
                
                standardColorName = etree.Element('standardColorName')
                standardColorName.text = product_part_schema.primary_color.color_name
                Color.append(standardColorName)            

                hex = etree.Element('hex')
                hex.text = product_part_schema.primary_color.hex
                Color.append(hex)            

                approximatePms = etree.Element('approximatePms')
                approximatePms.text = product_part_schema.primary_color.approximate_pms
                Color.append(approximatePms)            

                colorName = etree.Element('colorName')
                colorName.text = product_part_schema.primary_color.color_name
                Color.append(colorName)       

                ColorArray.append(Color)

            ProductPart.append(ColorArray)

            primaryMaterial = etree.Element('primaryMaterial', xmlns=xmlns_shared_objects)
            primaryMaterial.text = product_part_schema.primary_material
            ProductPart.append(primaryMaterial)



            SpecificationArray = etree.Element('SpecificationArray')
            for specification in product_part_schema.specification_array:
                # Color = etree.Element('Color', xmlns=xmlns_shared_objects)
                # Color.text = color.


                Specification = etree.Element('Specification', xmlns=xmlns_shared_objects)
                
                specificationType = etree.Element('specificationType')
                specificationType.text = specification.specification_type
                Specification.append(specificationType)
                
                SpecificationUom = etree.Element('SpecificationUom')
                SpecificationUom.text = str(specification.specification_uom)
                Specification.append(SpecificationUom)

                measurementValue = etree.Element('measurementValue')
                measurementValue.text = str(specification.measurement_value)
                Specification.append(measurementValue)


                SpecificationArray.append(Specification)

            ProductPart.append(SpecificationArray)

            shape = etree.Element('shape', xmlns=xmlns_shared_objects)
            shape.text = product_part_schema.shape
            ProductPart.append(shape)

            ApparelSize = etree.Element('ApparelSize', xmlns=xmlns_shared_objects)
            # ApparelSize.text = product_part_schema.apparel_size

            apparelStyle = etree.Element('apparelStyle')
            apparelStyle.text = product_part_schema.apparel_size.apparel_style
            ApparelSize.append(apparelStyle)

            labelSize = etree.Element('labelSize')
            labelSize.text = product_part_schema.apparel_size.label_size
            ApparelSize.append(labelSize)

            customSize = etree.Element('customSize')
            customSize.text = product_part_schema.apparel_size.custom_size
            ApparelSize.append(customSize)


            ProductPart.append(ApparelSize)


            Dimension = etree.Element('Dimension', xmlns=xmlns_shared_objects)

            dimensionUom = etree.Element('dimensionUom')
            dimensionUom.text = product_part_schema.dimension.dimension_uom
            Dimension.append(dimensionUom)

            dimensionUom = etree.Element('dimensionUom')
            dimensionUom.text = product_part_schema.dimension.dimension_uom
            Dimension.append(dimensionUom)

            depth = etree.Element('depth')
            depth.text = str(product_part_schema.dimension.depth)
            Dimension.append(depth)

            height = etree.Element('height')
            height.text = str(product_part_schema.dimension.height)
            Dimension.append(height)

            width = etree.Element('width')
            width.text = str(product_part_schema.dimension.width)
            Dimension.append(width)

            weightUom = etree.Element('weightUom')
            weightUom.text = str(product_part_schema.dimension.weight_uom)
            Dimension.append(weightUom)

            weight = etree.Element('weight')
            weight.text = str(product_part_schema.dimension.weight)
            Dimension.append(weight)

            ProductPart.append(Dimension)


            lead_time = etree.Element('leadTime')
            lead_time.text = str(product_part_schema.lead_time)
            ProductPart.append(lead_time)

            unspsc = etree.Element('unspsc', xmlns=xmlns_shared_objects)
            unspsc.text = str(product_part_schema.unspsc)
            ProductPart.append(unspsc)

            gtin = etree.Element('gtin', xmlns=xmlns_shared_objects)
            gtin.text = str(product_part_schema.gtin)
            ProductPart.append(gtin)

            isRushService = etree.Element('isRushService', xmlns=xmlns_shared_objects)
            isRushService.text = str(product_part_schema.is_rush_service).lower()
            ProductPart.append(isRushService)


            ProductPackagingArray = etree.Element('ProductPackagingArray')
            for product_package in product_part_schema.product_packaging_array:
                ProductPackage = etree.Element('ProductPackage', xmlns=xmlns_shared_objects)

                default = etree.Element('default')
                default.text = str(product_package.default)
                ProductPackage.append(default)
                
                packageType = etree.Element('packageType')
                packageType.text = product_package.package_type
                ProductPackage.append(packageType)

                description = etree.Element('description')
                description.text = product_package.description
                ProductPackage.append(description)
                
                quantity = etree.Element('quantity')
                quantity.text = str(product_package.quantity)
                ProductPackage.append(quantity)

                dimensionUom = etree.Element('dimensionUom')
                dimensionUom.text = str(product_package.dimension_uom)
                ProductPackage.append(dimensionUom)
                
                depth = etree.Element('depth')
                depth.text = str(product_package.depth)
                ProductPackage.append(depth)
                
                height = etree.Element('height')
                height.text = str(product_package.height)
                ProductPackage.append(height)
                
                width = etree.Element('width')
                width.text = str(product_package.width)
                ProductPackage.append(width)
                
                weightUom = etree.Element('weightUom')
                weightUom.text = product_package.weight_uom
                ProductPackage.append(weightUom)

                weight = etree.Element('weight')
                weight.text = str(product_package.weight)
                ProductPackage.append(weight)

                ProductPackagingArray.append(ProductPackage)

            ProductPart.append(ProductPackagingArray)


            ShippingPackageArray = etree.Element('ShippingPackageArray')
            for product_package in product_part_schema.shipping_packaging_array:
                ShippingPackage = etree.Element('ShippingPackage', xmlns=xmlns_shared_objects)

                # default = etree.Element('default')
                # default.text = str(product_package.default)
                # ShippingPackage.append(default)
                
                packageType = etree.Element('packageType')
                packageType.text = product_package.package_type
                ShippingPackage.append(packageType)

                description = etree.Element('description')
                description.text = product_package.description
                ShippingPackage.append(description)
                
                quantity = etree.Element('quantity')
                quantity.text = str(product_package.quantity)
                ShippingPackage.append(quantity)

                dimensionUom = etree.Element('dimensionUom')
                dimensionUom.text = str(product_package.dimension_uom)
                ShippingPackage.append(dimensionUom)
                
                
                depth = etree.Element('depth')
                depth.text = str(product_package.depth)
                ShippingPackage.append(depth)
                
                height = etree.Element('height')
                height.text = str(product_package.height)
                ShippingPackage.append(height)
                
                width = etree.Element('width')
                width.text = str(product_package.width)
                ShippingPackage.append(width)
                
                weightUom = etree.Element('weightUom')
                weightUom.text = product_package.weight_uom
                ShippingPackage.append(weightUom)

                weight = etree.Element('weight')
                weight.text = str(product_package.weight)
                ShippingPackage.append(weight)


                ShippingPackageArray.append(ShippingPackage)
            ProductPart.append(ShippingPackageArray)
            
            ProductPartArray.append(ProductPart) 

    root.append(ProductPartArray)

    lastChangeDate = etree.Element('lastChangeDate')
    lastChangeDate.text = str(product_data.last_change_date)
    root.append(lastChangeDate)

    creationDate = etree.Element('creationDate')
    creationDate.text = str(product_data.creation_date)
    root.append(creationDate)

    endDate = etree.Element('endDate', xmlns=xmlns_shared_objects)
    endDate.text = str(product_data.end_date)
    root.append(endDate)

    effectiveDate = etree.Element('effectiveDate', xmlns=xmlns_shared_objects)
    effectiveDate.text = str(product_data.effective_date)
    root.append(effectiveDate)

    isCaution = etree.Element('isCaution', xmlns=xmlns_shared_objects)
    isCaution.text = str(product_data.is_caution)
    root.append(isCaution)

    cautionComment = etree.Element('cautionComment', xmlns=xmlns_shared_objects)
    cautionComment.text = product_data.caution_comment
    root.append(cautionComment)

    isCloseout = etree.Element('isCloseout', xmlns=xmlns_shared_objects)
    isCloseout.text = str(product_data.is_closeout)
    root.append(isCloseout)

    lineName = etree.Element('lineName', xmlns=xmlns_shared_objects)
    lineName.text = product_data.line_name
    root.append(lineName)
    
    defaultSetupCharge = etree.Element('defaultSetupCharge', xmlns=xmlns_shared_objects)
    defaultSetupCharge.text = product_data.default_set_up_charge
    root.append(defaultSetupCharge)

    defaultRunCharge = etree.Element('defaultRunCharge', xmlns=xmlns_shared_objects)
    defaultRunCharge.text = product_data.default_run_charge
    root.append(defaultRunCharge)

    imprintSize = etree.Element('imprintSize', xmlns=xmlns_shared_objects)
    imprintSize.text = product_data.default_run_charge
    root.append(imprintSize)

    FobPointArray = etree.Element('FobPointArray', xmlns=xmlns_shared_objects)
    product_data.fob_point_array = json.loads(product_data.fob_point_array)

    print (product_data.fob_point_array)

    if product_data.fob_point_array:
        for fob_point in product_data.fob_point_array:
            fob_point_schema = schemas.FobPoint(**fob_point)
            FobPoint = etree.Element('FobPoint')

            fobId = etree.Element('fobId')
            fobId.text = fob_point_schema.fob_id
            FobPoint.append(fobId)

            fobCity = etree.Element('fobCity')
            fobCity.text = fob_point_schema.fob_city
            FobPoint.append(fobCity)

            fobState = etree.Element('fobState')
            fobState.text = fob_point_schema.fob_state
            FobPoint.append(fobState)

            fobPostalCode = etree.Element('fobPostalCode')
            fobPostalCode.text = fob_point_schema.fob_postal_code
            FobPoint.append(fobPostalCode)

            fobCountry = etree.Element('fobCountry')
            fobCountry.text = fob_point_schema.fob_country
            FobPoint.append(fobCountry)

            FobPointArray.append(FobPoint)


    root.append(FobPointArray)


    # isCloseout = etree.Element('isCloseout', xmlns=xmlns_shared_objects)
    # isCloseout.text = product_data.is_closeout
    # root.append(isCloseout)













    # xhtml = etree.Element("{http://www.w3.org/1999/xhtml}html")
    # body = etree.SubElement(xhtml, "{http://www.w3.org/1999/xhtml}body")
    # body.text = "Hello World"
    # root.append(xhtml)





    # ProductName.text = product_data.product_name
    # root.append(ProductName)



    xml = etree.tostring(root, pretty_print=True)
    return xml
