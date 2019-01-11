from flask import request
from flask_restful import reqparse, Resource
from common.dao import wfday_query, locality_query

class WfDay(Resource):

    def get(self, id=None, locality_id=None):

        if not id and locality_id:
            wfdays = wfday_query.get_wf_day(locality_id)
            if wfdays:
                body = {
                    'success': True,
                    'wfdays': wfdays
                }
                return body, 200

        elif not locality_id and id:
            wfday = wfday_query.get_wf_day_byid(id)
            if wfday:
                body = {
                    'success': True,
                    'wfday': wfday
                }
                return body, 200
            else:
                body = {
                    'success': False,
                    'message': 'weather forecasting day id ' + str(id) + ' not found in database'
                }
                return body, 409

        body = {
            'success': True,
            'message': 'error to list'
        }
        return body, 500

    def post(self):
        '''
            +---------------+---------+------+-----+---------+----------------+
            | Field         | Type    | Null | Key | Default | Extra          |
            +---------------+---------+------+-----+---------+----------------+
            | id            | int(11) | NO   | PRI | NULL    | auto_increment |
            | weather       | text    | NO   |     | NULL    |                |
            | precipitation | int(11) | NO   |     | NULL    |                |
            | date          | date    | NO   |     | NULL    |                |
            | max           | int(11) | NO   |     | NULL    |                |
            | min           | int(11) | NO   |     | NULL    |                |
            | locality_id   | int(11) | NO   | MUL | NULL    |                |
            | lag           | int(11) | NO   |     | NULL    |                |
            +---------------+---------+------+-----+---------+----------------+
        '''

        post_parser = reqparse.RequestParser()
        post_parser.add_argument(
            'weather', dest='weather',
            type=str, required=True, help='required field <atmospheric_pressure> not informed.',
        )
        post_parser.add_argument(
            'precipitation', dest='precipitation',
            type=int, required=True, help='required field <precipitation> not informed',
        )
        post_parser.add_argument(
            'date', dest='date',
            type=str, required=True, help='required field <date> not informed',
        )
        post_parser.add_argument(
            'max', dest='max',
            type=int, required=True, help='required field <max> not informed',
        )
        post_parser.add_argument(
            'min', dest='min',
            type=int, required=True, help='required field <min> not informed',
        )
        post_parser.add_argument(
            'locality_id', dest='locality_id',
            type=int, required=True, help='required field <locality_id> not informed',
        )
        post_parser.add_argument(
            'lag', dest='lag',
            type=int, required=True, help='required field <lag> not informed',
        )

        data = dict()
        args = post_parser.parse_args()

        if not locality_query.consult_locality_byid(args.locality_id):
            body = {
                'success': False,
                'message': 'locality id ' + str(args.locality_id) + ' not found in database'
            }
            return body, 409

        data['weather'] = args.weather
        data['precipitation'] = args.precipitation
        data['date'] = args.date
        data['max'] = args.max
        data['min'] = args.min
        data['locality_id'] = args.locality_id
        data['lag'] = args.lag

        if wfday_query.create_wfday(data):
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

    def put(self, id=None):
        '''
            +---------------+---------+------+-----+---------+----------------+
            | Field         | Type    | Null | Key | Default | Extra          |
            +---------------+---------+------+-----+---------+----------------+
            | id            | int(11) | NO   | PRI | NULL    | auto_increment |
            | weather       | text    | NO   |     | NULL    |                |
            | precipitation | int(11) | NO   |     | NULL    |                |
            | date          | date    | NO   |     | NULL    |                |
            | max           | int(11) | NO   |     | NULL    |                |
            | min           | int(11) | NO   |     | NULL    |                |
            | locality_id   | int(11) | NO   | MUL | NULL    |                |
            | lag           | int(11) | NO   |     | NULL    |                |
            +---------------+---------+------+-----+---------+----------------+
        '''

        put_parser = reqparse.RequestParser()
        put_parser.add_argument(
            'weather', dest='weather',
            type=str, required=True, help='required field <atmospheric_pressure> not informed.',
        )
        put_parser.add_argument(
            'precipitation', dest='precipitation',
            type=int, required=True, help='required field <precipitation> not informed',
        )
        put_parser.add_argument(
            'date', dest='date',
            type=str, required=True, help='required field <date> not informed',
        )
        put_parser.add_argument(
            'max', dest='max',
            type=int, required=True, help='required field <max> not informed',
        )
        put_parser.add_argument(
            'min', dest='min',
            type=int, required=True, help='required field <min> not informed',
        )
        put_parser.add_argument(
            'locality_id', dest='locality_id',
            type=int, required=True, help='required field <locality_id> not informed',
        )

        data = dict()
        args = put_parser.parse_args()

        if not locality_query.consult_locality_byid(args.locality_id):
            body = {
                'success': False,
                'message': 'locality id ' + str(args.locality_id) + ' not found in database'
            }
            return body, 409


        if not wfday_query.get_wf_day_byid(id):
            body = {
                'success': False,
                'message': 'weather forecating day id ' + str(id) + ' not found in database'
            }
            return body, 409

        data['id'] = id
        data['weather'] = args.weather
        data['precipitation'] = args.precipitation
        data['date'] = args.date
        data['max'] = args.max
        data['min'] = args.min
        data['locality_id'] = args.locality_id

        if wfday_query.update_wfday(data):
            body = {
                'success': True,
                'message': 'updated with successfully!',
            }
            return body, 200

        body = {
            'success': False,
            'message': 'error to update'
        }
        return body, 500

    def delete(self, id=None):
        
        if not wfday_query.get_wf_day_byid(id):
            body = {
                'success': False,
                'message': 'weather forecating day id ' + str(id) + ' not found in database'
            }
            return body, 409

        if wfday_query.delete_wfday(id):
            body = {
                'success': True,
                'message': 'deleted with successfully!',
            }
            return body, 200

        body = {
            'success': False,
            'message': 'error to delete'
        }
        return body, 500