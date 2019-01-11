import os
import pandas as pd
from lib_formatter_logger import log
from common.dao import querys
from config import LOG_NAME

CITIES_CSV = os.getcwd() + '/csv/climatempo_all_cities.csv'
logger = log.getLogger(LOG_NAME)

def import_cities():
    '''

    '''
    brasil = 1
    states = querys.get_all_regions(brasil)
    cities = pd.read_csv(CITIES_CSV, sep=',', header=0, names=['state_code', 'city_name'])

    logger.info('registering all cities...')
    for state in states:
        for idx, city in cities.iterrows():
            if state['code'] == city.state_code:
                parameters = dict()
                parameters['name'] = city.city_name
                parameters['region_id'] = state['id']
                querys.create_locality(parameters)

import_cities()





