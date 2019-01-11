from flask import request
from flask_restful import reqparse, Resource
from common.dao import locality_query

class Localities(Resource):
     
    def get(self, region_id=None, locality_id=None):

        if not locality_id and region_id:
            localities = locality_query.get_all_localities(region_id)
            if not localities:
                msg = 'region id ' + str(region_id) + ' not found in database'
                body = {
                    'success': False,
                    'message': msg
                }
                return body, 409

            body = {
                'success': True,
                'localities': localities
            }
            return body, 200

        elif locality_id and not region_id:
            locality = locality_query.consult_locality_byid(locality_id)
            if not locality:
                msg = 'locality id ' + str(locality_id) + ' not found in database'
                body = {
                    'success': False,
                    'message': msg
                }
                return body, 409

            body = {
                'success': True,
                'locality': locality
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
            type=str, required=True, help='required field <name> not informed in locality.',
        )
        post_parser.add_argument(
            'region_id', dest='region_id',
            type=int, required=True, help='required field <region_id> not informed in locality.',
        )
        
        data = dict()
        args = post_parser.parse_args()
        if locality_query.consult_locality_byname(args.name, args.region_id):
            body = {
                'success': False,
                'message': 'name locality already registered!'
            }
            return body, 200

        data['region_id'] = args.region_id
        data['name'] = args.name
        if locality_query.create_locality(data):
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

    def put(self, locality_id=None):
    
        put_parser = reqparse.RequestParser()
        put_parser.add_argument(
            'name', dest='name',
            type=str, required=True, help='required field <name> not informed in locality.',
        )
        put_parser.add_argument(
            'region_id', dest='region_id',
            type=int, required=True, help='required field <region_id> not informed in locality.',
        )
        
        data = dict()
        args = put_parser.parse_args()

        if not locality_query.consult_locality_byid(locality_id):
            body = {
                'success': False,
                'message': 'region id ' + str(locality_id) + ' not found in database'
            }
            return body, 409

        if locality_query.consult_locality_byname(args.name, args.region_id):
            body = {
                'success': False,
                'message': 'name locality already registered!'
            }
            return body, 200

        data['id'] = locality_id
        data['region_id'] = args.region_id
        data['name'] = args.name
        if locality_query.update_locality(data):
            body = {
                'success': True,
                'message': 'update with successfully!',
            }
            return body, 200

        body = {
            'success': False,
            'message': 'error to update'
        }
        return body, 500