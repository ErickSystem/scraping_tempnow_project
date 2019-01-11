from flask import request
from flask_restful import reqparse, Resource
from common.dao import country_query

class Countries(Resource):

    def get(self, id=None):

        if not id:
            countries = country_query.get_all_country()
            if countries:
                body = {
                    'success': True,
                    'countries': countries
                }
                return body, 200

        else:
            country = country_query.get_country_byid(id)
            if not country:
                msg = 'country id ' + str(id) + ' not found in database'
                body = {
                    'message': msg,
                    'success': False
                }
                return body, 409

            body = {
                'success': True,
                'country': country
            }
            return body, 200
   
        body = {
            'success': False,
            'message': 'was not possible to list'
        }
        return body, 500



