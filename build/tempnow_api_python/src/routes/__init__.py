from flask import Blueprint
from flask_restful import Api

# RESOURCES
from resources.country import Countries
from resources.region import Regions
from resources.locality import Localities
from resources.wfhour import WfHour
from resources.wfday import WfDay

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# COUNTRIES
api.add_resource(
    Countries, 
    '/countries',
    '/countries/<int:id>'
)

# REGIONS
api.add_resource(
    Regions,
    '/regions',
    '/regions/<int:country_id>',
    '/regions/<int:region_id>/region'
)

# LOCALITY 
api.add_resource(
    Localities,
    '/localities',
    '/localities/<int:region_id>',
    '/localities/<int:locality_id>/locality'
)

# WEATHER FORECASTING HOUR
api.add_resource(
    WfHour,
    '/wfhours',
    '/wfhours/<int:locality_id>',
    '/wfhours/<int:id>/wfhour'
)

# WEATHER FORECASTING DAY
api.add_resource(
    WfDay,
    '/wfdays',
    '/wfdays/<int:locality_id>',
    '/wfdays/<int:id>/wfday'
)