from lib_formatter_logger import log
from config import LOG_NAME
logger = log.getLogger(LOG_NAME)
try:
    from common.datasource.connection import MYSQL
except Exception as e:
    logger.error("error to import the database class MYSQL | %s", e)
    exit(1)

def get_wf_hour(locality_id):
    '''

    '''
    params = {
        'locality_id': locality_id
    }

    query = """
        SELECT 
            wf.id,
            wf.atmospheric_pressure,
            wf.wind,
            wf.temp,
            wf.relative_humidity,
            wf.last_update,
            wf.weather,
            wf.locality_id,
            wf.date_time,
            l.`name` as locality_name,
            r.`name` as region_name,
            r.`code`
        FROM `weather_forecasting_hour` wf
        JOIN locality l ON l.id = wf.locality_id
        JOIN region r ON r.id = l.region_id
        WHERE
            l.id = :locality_id
        ORDER BY
            wf.date_time;
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult weather forecasting hour by locality_id")
        return False

    if MYSQL.result:
        return MYSQL.result

    return False

def get_wf_hour_byid(id):
    '''

    '''
    params = {
        'id': id
    }

    query = """
        SELECT 
            id,
            atmospheric_pressure,
            wind,
            temp,
            relative_humidity,
            last_update,
            weather,
            locality_id,
            date_time
        FROM `weather_forecasting_hour`
        WHERE
            id = :id
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult weather forecasting hour by id")
        return False

    if MYSQL.result:
        return {
            'id': MYSQL.result[0]['id'],
            'atmospheric_pressure': MYSQL.result[0]['atmospheric_pressure'],
            'wind': MYSQL.result[0]['wind'],
            'temp': MYSQL.result[0]['temp'],
            'relative_humidity': MYSQL.result[0]['relative_humidity'],
            'last_update': MYSQL.result[0]['last_update'],
            'weather': MYSQL.result[0]['weather'],
            'locality_id': MYSQL.result[0]['locality_id'],
            'date_time': MYSQL.result[0]['date_time']
        }
    return False


def create_wfhour(parameters):
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
        
        RETURN:
            bool
    '''
    params = {
        'atmospheric_pressure': parameters['atmospheric_pressure'],
        'wind': parameters['wind'],
        'temp': parameters['temp'],
        'relative_humidity': parameters['relative_humidity'],
        'last_update': parameters['last_update'],
        'weather': parameters['weather'],
        'locality_id': parameters['locality_id'],
        'date_time': parameters['date_time']
    }

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
    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to create weather forecasting hour")
        return False

    logger.info("weather forecasting hour created with successfully!")
    return True

def update_wfhour(parameters):
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
        
        RETURN:
            bool
    '''
    params = {
        'id': parameters['id'],
        'atmospheric_pressure': parameters['atmospheric_pressure'],
        'wind': parameters['wind'],
        'temp': parameters['temp'],
        'relative_humidity': parameters['relative_humidity'],
        'last_update': parameters['last_update'],
        'weather': parameters['weather'],
        'locality_id': parameters['locality_id'],
        'date_time': parameters['date_time']
    }

    query = 'UPDATE `weather_forecasting_hour` SET `atmospheric_pressure` = :atmospheric_pressure, \
                `wind` = :wind, \
                `temp` = :temp, \
                `relative_humidity` = :relative_humidity, \
                `last_update` = :last_update, \
                `weather` = :weather, \
                `locality_id` = :locality_id, \
                `date_time` = :date_time \
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

def delete_wfhour(id):
    '''

    '''
    params = {
        'id': id
    }

    query = 'DELETE FROM `weather_forecasting_hour` WHERE id = :id'

    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to delete weather forecasting hour")
        return False

    logger.debug("weather forecasting hour deleted with successfully!")
    return True