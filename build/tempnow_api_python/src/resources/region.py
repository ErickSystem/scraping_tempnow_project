from flask import request
from flask_restful import reqparse, Resource
from common.dao import region_query

class Regions(Resource):
     
    def get(self, country_id=None, region_id=None):

        if not region_id and country_id:
            regions = region_query.get_all_regions(country_id)
            if not regions:
                msg = 'country id ' + str(country_id) + ' not found in database'
                body = {
                    'success': False,
                    'message': msg
                }
                return body, 200

            body = {
                'success': True,
                'regions': regions
            }
            return body, 200
 
        if region_id and not country_id:
            region = region_query.consult_region_byid(region_id)
            if not region:
                msg = 'region id ' + str(region_id) + ' not found in database'
                body = {
                    'success': False,
                    'message': msg
                }
                return body, 409

            body = {
                'success': True,
                'region': region
            }
            return body, 200
        
        body = {
            'success': False,
            'message': 'was not possible to list'
        }
        return body, 500

    def post(self):
    
        post_parser = reqparse.RequestParser()
        post_parser.add_argument(
            'name', dest='name',
            type=str, required=True, help='required field <name> not informed.'
        )
        post_parser.add_argument(
            'code', dest='code',
            type=str, required=True, help='required field <code> not informed'
        )
        post_parser.add_argument(
            'default_timezone', dest='default_timezone',
            type=str, required=True, help='required field <default_timezone> not informed'
        )
        post_parser.add_argument(
            'country_id', dest='country_id',
            type=int, required=True, help='required field <country_id> not informed'
        )
        
        data = dict()
        args = post_parser.parse_args()

        data['name'] = args.name
        data['code'] = args.code
        data['default_timezone'] = args.default_timezone
        data['country_id'] = args.country_id
        if region_query.create_region(data):
            body = {
                'success': True,
                'message': 'created with successfully!',
            }
            return body, 201

        body = {
            'success': False,
            'message': 'error to create'
        }
        return body, 500

    def put(self, region_id=None):
        
        put_parser = reqparse.RequestParser()
        put_parser.add_argument(
            'name', dest='name',
            type=str, required=True, help='required field <name> not informed.',
        )
        put_parser.add_argument(
            'code', dest='code',
            type=str, required=True, help='required field <code> not informed',
        )
        put_parser.add_argument(
            'default_timezone', dest='default_timezone',
            type=str, required=True, help='required field <default_timezone> not informed',
        )
        put_parser.add_argument(
            'country_id', dest='country_id',
            type=int, required=True, help='required field <country_id> not informed',
        )
        
        data = dict()
        args = put_parser.parse_args()

        if not region_query.consult_region_byid(region_id):
            body = {
                'success': False,
                'message': 'region id ' + str(region_id) + ' not found in database'
            }
            return body, 409

        data['id'] = region_id
        data['name'] = args.name
        data['code'] = args.code
        data['default_timezone'] = args.default_timezone
        data['country_id'] = args.country_id
        if region_query.update_region(data):
            body = {
                'success': True,
                'message': 'updated with successfully!',
            }
            return body, 201

        body = {
            'success': False,
            'message': 'error to updated'
        }
        return body, 500