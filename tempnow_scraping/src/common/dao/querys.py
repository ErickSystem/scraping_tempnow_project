from datetime import datetime
from lib_formatter_logger import log
from config import LOG_NAME
logger = log.getLogger(LOG_NAME)
try:
    from common.datasource.connection import MYSQL
except Exception as e:
    logger.error("error to import the database class MYSQL | %s", e)
    exit(1)

######################## REGIONS #####################################

def get_all_regions(country_id):
    """Retorna todos os estados por país"""

    params = {'country_id': country_id}

    query = """
        SELECT 
            id,
            name,
            code,
            default_timezone,
            country_id
        FROM `region`
        WHERE
            country_id = :country_id
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult regions in databases")
        return []

    if MYSQL.result:
        return MYSQL.result

    logger.warning('failed consult all regions')
    return []

############ LOCALITY ################

def consult_locality_byregionid(region_id):
    """Retorna todos os estados por país"""

    params = {'region_id': region_id}

    query = """
        SELECT 
            id,
            name
        FROM `locality`
        WHERE
            region_id = :region_id
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult locality in databases")
        return []

    if MYSQL.result:
        return MYSQL.result

    logger.warning('failed consult cities by region id')
    return []

def create_locality(parameters):
    '''

    '''
    params = {
        'name': parameters['name'],
        'region_id': parameters['region_id']
    }

    query = """
        INSERT INTO `locality`(
                name, 
                region_id
            )
	    VALUES(
            :name,
            :region_id
            );
    """
    logger.debug("creating locality...")
    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to create locality")
        return False

    return True

####################### WEATHER FORECASTING HOUR ###############################

def exist_wfhour(locality_id, date_time, conn=None):
    '''

    '''
    params = {
        'locality_id': locality_id,
        'date_time': date_time
    }

    query = """
        SELECT * 
        FROM weather_forecasting_hour
        WHERE
            locality_id = :locality_id
            AND date_time = :date_time;
    """
    if conn:
        try:
            MYSQL.session_execute(
                query=query,
                params=params,
                connection=conn,
            )
        except:
            return False
    else:
        try:
            MYSQL.execute(
                query=query,
                params=params
            )
        except:
            return False

    if MYSQL.result:
        return True

    return True

def create_wfhour(parameters, conn=None):
    '''

    '''
    params = {
        'locality_id': parameters['locality_id'], 
        'temp': parameters['temp'], 
        'weather': parameters['weather'], 
        'last_update': parameters['last_update'], 
        'wind': parameters['wind'], 
        'atmospheric_pressure': parameters['atmospheric_pressure'], 
        'relative_humidity': parameters['relative_humidity'],
        'date_time': parameters['date_time']
    }

    if exist_wfhour(params['locality_id'], params['date_time'], conn):
        logger.info('weather forecasting hour alread exist: [{0}] '.format(parameters))
        return True

    query = """
        INSERT INTO `weather_forecasting_hour`(
                atmospheric_pressure,
                wind,
                temp,
                relative_humidity,
                last_update,
                weather,
                locality_id,
                date_time
            )
	    VALUES(
            :atmospheric_pressure,
            :wind,
            :temp,
            :relative_humidity,
            :last_update,
            :weather,
            :locality_id,
            :date_time
            );
    """
    if conn:
        try:
            MYSQL.session_execute(
                query=query,
                params=params,
                connection=conn,
                get_results=False,
                check_for_empty_result=False
            )
        except:
            logger.exception("error to create weather forecasting: [{}]".format(parameters))
            return False
    else:
        try:
            MYSQL.execute(
                query=query,
                params=params,
                get_results=False,
                check_for_empty_result=False
            )
        except:
            logger.exception("error to create weather forecasting: [{}]".format(parameters))
            return False

    logger.info('weather forecasting hour created with successfully!')
    return True

####################### WEATHER FORECASTING DAY ###############################

def exist_wfday(locality_id, date, conn=None):
    '''

    '''
    params = {
        'locality_id': locality_id,
        'date': date
    }

    query = """
        SELECT * 
        FROM weather_forecasting_day
        WHERE
            locality_id = :locality_id
            AND date = :date;
    """
    if conn:
        try:
            MYSQL.session_execute(
                query=query,
                params=params,
                connection=conn,
            )
        except:
            return False
    else:
        try:
            MYSQL.execute(
                query=query,
                params=params
            )
        except:
            return False

    if MYSQL.result:
        return True

    return True

def consult_wfday(locality_id, date, conn=None):
    '''

    '''
    params = {
        'locality_id': locality_id,
        'date': date
    }

    query = """
        SELECT * 
        FROM weather_forecasting_day
        WHERE
            locality_id = :locality_id
            AND date = :date;
    """
    if conn:
        try:
            MYSQL.session_execute(
                query=query,
                params=params,
                connection=conn,
            )
        except:
            return False
    else:
        try:
            MYSQL.execute(
                query=query,
                params=params
            )
        except:
            return False

    if MYSQL.result:
        return {
            'id': MYSQL.result[0]['id'],
            'weather': MYSQL.result[0]['weather'],
            'precipitation': MYSQL.result[0]['precipitation'],
            'date': MYSQL.result[0]['date'],
            'max': MYSQL.result[0]['max'],
            'min': MYSQL.result[0]['min'],
            'locality_id': MYSQL.result[0]['locality_id'],
            'lag': MYSQL.result[0]['lag']
        }

def consult_lag(locality_id, conn=None):
    '''

    '''
    params = {
        'locality_id': locality_id
    }

    query = """
        SELECT 
            lag 
        FROM weather_forecasting_day
        WHERE
            locality_id = :locality_id
    """
    if conn:
        try:
            MYSQL.session_execute(
                query=query,
                params=params,
                connection=conn,
            )
        except:
            return False
    else:
        try:
            MYSQL.execute(
                query=query,
                params=params
            )
        except:
            return False

    if MYSQL.result:
        return MYSQL.result

def create_wfday(parameters, conn=None):
    '''

    '''
    params = {
        'locality_id': parameters['locality_id'], 
        'precipitation': parameters['precipitation'], 
        'weather': parameters['weather'], 
        'date': parameters['date'], 
        'max': parameters['max'], 
        'min': parameters['min'], 
        'lag': parameters['lag'],
    }

    if exist_wfday(params['locality_id'], params['date'], conn):
        return True

    query = """
        INSERT INTO `weather_forecasting_day`(
            weather,
            precipitation,
            `date`,
            `max`,
            `min`,
            locality_id,
            lag

        )
	    VALUES(
            :weather,
            :precipitation,
            :date,
            :max,
            :min,
            :locality_id,
            :lag
        );
    """
    if conn:
        try:
            MYSQL.session_execute(
                query=query,
                params=params,
                connection=conn,
                get_results=False,
                check_for_empty_result=False
            )
        except:
            logger.exception("error to create weather forecasting: [{}]".format(parameters))
            return False
    else:
        try:
            MYSQL.execute(
                query=query,
                params=params,
                get_results=False,
                check_for_empty_result=False
            )
        except:
            logger.exception("error to create weather forecasting: [{}]".format(parameters))
            return False

    logger.info('weather forecasting day created with successfully!')
    return True

def update_wfday(parameters, conn=None):
    '''

    '''
    params = {
        'id': parameters['id'],
        'locality_id': parameters['locality_id'], 
        'precipitation': parameters['precipitation'], 
        'weather': parameters['weather'], 
        '_date': parameters['date'], 
        '_max': parameters['max'], 
        '_min': parameters['min'], 
        'lag': parameters['lag'],
    }
    query = 'UPDATE `weather_forecasting_day` SET weather = :weather, \
            precipitation = :precipitation, \
            `max` = :_max, \
            `min` = :_min, \
            `date` = :_date, \
            locality_id = :locality_id, \
            lag = :lag \
            WHERE id = :id'

    if conn:
        try:
            MYSQL.session_execute(
                query=query,
                params=params,
                connection=conn,
                get_results=False,
                check_for_empty_result=False
            )
        except:
            logger.exception("error to update weather forecasting: [{}]".format(parameters))
            return False
    else:
        try:
            MYSQL.execute(
                query=query,
                params=params,
                get_results=False,
                check_for_empty_result=False
            )
        except:
            logger.exception("error to update weather forecasting: [{}]".format(parameters))
            return False

    logger.info('weather forecasting day updated with successfully!')
    return True