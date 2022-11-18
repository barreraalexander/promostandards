from flask import Blueprint, redirect, url_for, request, jsonify
import xmltodict

router = Blueprint('api', __name__, url_prefix='/api')

# request parameters need to be xml
# returns need to be xml

@router.route('/inventory')
def inventory():
    # print (request)
    # print (dir(request))

    # print (request.method)
    request_xml = request.data




    # print (request_xml)
    # xml_dict = xmltodict.parse(request_xml)
    # print (xml_dict)


    # custom_dict = {
    #     'env:Envelope' : {
    #         '@xmlns:env' : 'http://schemas.xmlsoap.org/soap/envelope/'

    #     }
    # }

    mock_product = {
        
    }


    custom_dict = {
        'env:Envelope': {
            '@xmlns:env': 'http://schemas.xmlsoap.org/soap/envelope/',
            'env:Body': {
                'GetRelevanceResult': {
                    '@xmlns': 'http://[webreportshostname]:[webreportsport]      /webreports?wsdl',
                    'relevanceExpr': 'names of bes computers', 'username': 'user', 'password': 'password'
                    }
                }
            }
        }

    custom_xml = xmltodict.unparse()

    print (custom_xml)

    return jsonify({'root' : 'root'})


                                                                                                                                

@router.route('/products')
def products():

    request_xml =  request.data
    xml_dict = xmltodict.parse(request)



    return 'hi'



@router.route('/media_content')
def media_content():
    pass


# product pricing and config
@router.route('/ppc')
def ppc():
    pass
    
