from lib_formatter_logger import log
from config import LOG_NAME
logger = log.getLogger(LOG_NAME)
try:
    from common.datasource.connection import MYSQL
except Exception as e:
    logger.error("error to import the database class MYSQL | %s", e)
    exit(1)

def consult_lag(locality_id):
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
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        return False

    if MYSQL.result:
        return MYSQL.result

def get_wf_day(locality_id):
    '''

    '''
    params = {
        'locality_id': locality_id
    }
    query = """
        SELECT 
            wf.id,
            wf.weather,
            wf.precipitation,
            wf.`date`,
            wf.`max`,
            wf.`min`,
            wf.locality_id,
            wf.lag,
            l.`name` as locality_name,
            r.`name` as region_name,
            r.`code`
        FROM `weather_forecasting_day` wf
        JOIN locality l ON l.id = wf.locality_id
        JOIN region r ON r.id = l.region_id
        WHERE
            l.id = :locality_id
        ORDER BY
            wf.`date`;
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult weather forecasting day by locality_id")
        return False

    if MYSQL.result:
        return MYSQL.result

    return False

def get_wf_day_byid(id):
    '''

    '''
    params = {
        'id': id
    }

    query = """
        SELECT 
            id,
            weather,
            precipitation,
            date,
            max,
            min,
            locality_id,
            lag
        FROM `weather_forecasting_day`
        WHERE
            id = :id
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult weather forecasting day by id")
        return False

    if MYSQL.result:
        return {
            'id': MYSQL.result[0]['id'],
            'weather': MYSQL.result[0]['weather'],
            'precipitation': MYSQL.result[0]['precipitation'],
            'date': MYSQL.result[0]['date'],
            'max': MYSQL.result[0]['max'],
            'min': MYSQL.result[0]['min'],
            'weather': MYSQL.result[0]['weather'],
            'locality_id': MYSQL.result[0]['locality_id'],
            'lag': MYSQL.result[0]['lag']
        }
    return False


def create_wfday(parameters):
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
        
        RETURN:
            bool
    '''
    params = {
        'precipitation': parameters['precipitation'],
        '_date': parameters['date'],
        '_max': parameters['max'],
        '_min': parameters['min'],
        'weather': parameters['weather'],
        'locality_id': parameters['locality_id'],
        'lag': parameters['lag']
    }

    query = """
        INSERT INTO `weather_forecasting_day`(
                precipitation,
                `date`,
                `max`,
                `min`,
                weather,
                locality_id,
                lag
            )
	    VALUES(
            :precipitation,
            :_date,
            :_max,
            :_min,
            :weather,
            :locality_id,
            :lag
        );
    """
    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to create weather forecasting day")
        return False

    logger.info("weather forecasting day created with successfully!")
    return True

def update_wfday(parameters):
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
        
        RETURN:
            bool
    '''
    params = {
        'id': parameters['id'],
        'precipitation': parameters['precipitation'],
        '_date': parameters['date'],
        '_max': parameters['max'],
        '_min': parameters['min'],
        'weather': parameters['weather'],
        'locality_id': parameters['locality_id']
    }

    query = 'UPDATE `weather_forecasting_day` SET `precipitation` = :precipitation, \
                `date` = :_date, \
                `max` = :_max, \
                `min` = :_min, \
                `weather` = :weather, \
                `locality_id` = :locality_id \
            WHERE id = :id'

    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to update weather forecasting hour")
        return False

    logger.debug("weather forecasting hour updated with successfully!")
    return True

def delete_wfday(id):
    '''

    '''
    params = {
        'id': id
    }

    query = 'DELETE FROM `weather_forecasting_day` WHERE id = :id'

    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to delete weather forecasting day")
        return False

    logger.debug("weather forecasting day deleted with successfully!")
    return True