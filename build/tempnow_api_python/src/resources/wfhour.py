from flask import request
from flask_restful import reqparse, Resource
from common.dao import wfhour_query, locality_query

class WfHour(Resource):

    def get(self, id=None, locality_id=None):

        if not id and locality_id:
            wfhours = wfhour_query.get_wf_hour(locality_id)
            if wfhours:
                body = {
                    'success': True,
                    'wfhours': wfhours
                }
                return body, 200

        elif not locality_id and id:
            wfhour = wfhour_query.get_wf_hour_byid(id)
            if wfhour:
                body = {
                    'success': True,
                    'wfhours': wfhour
                }
                return body, 200
            else:
                body = {
                    'success': False,
                    'message': 'weather forecasting hour id ' + str(id) + ' not found in database'
                }
                return body, 409

        body = {
            'success': True,
            'message': 'error to list'
        }
        return body, 500

    def post(self):
        '''
            +----------------------+----------+------+-----+---------+----------------+
            | Field                | Type     | Null | Key | Default | Extra          |
            +----------------------+----------+------+-----+---------+----------------+
            | id                   | int(11)  | NO   | PRI | NULL    | auto_increment |
            | atmospheric_pressure | int(11)  | NO   |     | NULL    |                |
            | wind                 | int(11)  | NO   |     | NULL    |                |
            | temp                 | int(11)  | NO   |     | NULL    |                |
            | relative_humidity    | int(11)  | NO   |     | NULL    |                |
            | last_update          | text     | YES  |     | NULL    |                |
            | weather              | text     | NO   |     | NULL    |                |
            | locality_id          | int(11)  | NO   | MUL | NULL    |                |
            | date_time            | datetime | NO   |     | NULL    |                |
            +----------------------+----------+------+-----+---------+----------------+
        '''

        post_parser = reqparse.RequestParser()
        post_parser.add_argument(
            'atmospheric_pressure', dest='atmospheric_pressure',
            type=int, required=True, help='required field <atmospheric_pressure> not informed.',
        )
        post_parser.add_argument(
            'wind', dest='wind',
            type=int, required=True, help='required field <wind> not informed',
        )
        post_parser.add_argument(
            'temp', dest='temp',
            type=int, required=True, help='required field <temp> not informed',
        )
        post_parser.add_argument(
            'relative_humidity', dest='relative_humidity',
            type=int, required=True, help='required field <relative_humidity> not informed',
        )
        post_parser.add_argument(
            'last_update', dest='last_update',
            type=str, default=None
        )
        post_parser.add_argument(
            'weather', dest='weather',
            type=str, required=True, help='required field <weather> not informed',
        )
        post_parser.add_argument(
            'locality_id', dest='locality_id',
            type=int, required=True, help='required field <locality_id> not informed',
        )
        post_parser.add_argument(
            'date_time', dest='date_time',
            type=str, required=True, help='required field <date_time> not informed',
        )
        data = dict()
        args = post_parser.parse_args()

        if not locality_query.consult_locality_byid(args.locality_id):
            body = {
                'success': False,
                'message': 'locality id ' + str(args.locality_id) + ' not found in database'
            }
            return body, 409

        data['atmospheric_pressure'] = args.atmospheric_pressure
        data['wind'] = args.wind
        data['temp'] = args.temp
        data['relative_humidity'] = args.relative_humidity
        data['last_update'] = args.last_update
        data['weather'] = args.weather
        data['locality_id'] = args.locality_id
        data['date_time'] = args.date_time

        if wfhour_query.create_wfhour(data):
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
            +----------------------+----------+------+-----+---------+----------------+
            | Field                | Type     | Null | Key | Default | Extra          |
            +----------------------+----------+------+-----+---------+----------------+
            | id                   | int(11)  | NO   | PRI | NULL    | auto_increment |
            | atmospheric_pressure | int(11)  | NO   |     | NULL    |                |
            | wind                 | int(11)  | NO   |     | NULL    |                |
            | temp                 | int(11)  | NO   |     | NULL    |                |
            | relative_humidity    | int(11)  | NO   |     | NULL    |                |
            | last_update          | text     | YES  |     | NULL    |                |
            | weather              | text     | NO   |     | NULL    |                |
            | locality_id          | int(11)  | NO   | MUL | NULL    |                |
            | date_time            | datetime | NO   |     | NULL    |                |
            +----------------------+----------+------+-----+---------+----------------+
        '''

        put_parser = reqparse.RequestParser()
        put_parser.add_argument(
            'atmospheric_pressure', dest='atmospheric_pressure',
            type=int, required=True, help='required field <atmospheric_pressure> not informed.',
        )
        put_parser.add_argument(
            'wind', dest='wind',
            type=int, required=True, help='required field <wind> not informed',
        )
        put_parser.add_argument(
            'temp', dest='temp',
            type=int, required=True, help='required field <temp> not informed',
        )
        put_parser.add_argument(
            'relative_humidity', dest='relative_humidity',
            type=int, required=True, help='required field <relative_humidity> not informed',
        )
        put_parser.add_argument(
            'last_update', dest='last_update',
            type=str, default=None
        )
        put_parser.add_argument(
            'weather', dest='weather',
            type=str, required=True, help='required field <weather> not informed',
        )
        put_parser.add_argument(
            'locality_id', dest='locality_id',
            type=int, required=True, help='required field <locality_id> not informed',
        )
        put_parser.add_argument(
            'date_time', dest='date_time',
            type=str, required=True, help='required field <date_time> not informed',
        )

        data = dict()
        args = put_parser.parse_args()

        if not locality_query.consult_locality_byid(args.locality_id):
            body = {
                'success': False,
                'message': 'locality id ' + str(args.locality_id) + ' not found in database'
            }
            return body, 409


        if not wfhour_query.get_wf_hour_byid(id):
            body = {
                'success': False,
                'message': 'weather forecating hour id ' + str(id) + ' not found in database'
            }
            return body, 409

        data['id'] = id
        data['atmospheric_pressure'] = args.atmospheric_pressure
        data['wind'] = args.wind
        data['temp'] = args.temp
        data['relative_humidity'] = args.relative_humidity
        data['last_update'] = args.last_update
        data['weather'] = args.weather
        data['locality_id'] = args.locality_id
        data['date_time'] = args.date_time

        if wfhour_query.update_wfhour(data):
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
        
        if not wfhour_query.get_wf_hour_byid(id):
            body = {
                'success': False,
                'message': 'weather forecating hour id ' + str(id) + ' not found in database'
            }
            return body, 409

        if wfhour_query.delete_wfhour(id):
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