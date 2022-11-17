from flask import Blueprint, redirect, url_for, request, jsonify

router = Blueprint('api', __name__, url_prefix='/api')

@router.route('/')
def home():
    return jsonify({'here' : 'theresss'})
# router.route('/api', methods=["GET"])
# def api_root():
#     return jsonify({'here' : 'there'})