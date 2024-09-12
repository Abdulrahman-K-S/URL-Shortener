from flask_restx import Namespace, Resource, fields
from flask import request
from ..controller import create_short_url, redirect_to_original

url_bp = Namespace('url_bp', description="URL Operations")

original_url_model = url_bp.model(
    'PostRequestBody',
    {
        'original_url': fields.String(required=True, description="The original URL to shorten")
    }
)

@url_bp.route('/api/', endpoint='create')
class Create(Resource):
    @url_bp.expect(original_url_model)
    def post(self):
        original_url = request.json.get('original_url')
        if not original_url:
            return {'message': 'original_url is required'}, 400
    
        shortened_url = create_short_url(original_url)
        return {'short_url': shortened_url}, 201
    
    def get(self):
        shortened_url = request.args.get('shortened_url')
        return redirect_to_original(shortened_url)
