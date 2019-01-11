from lib_formatter_logger import log
from config import LOG_NAME
logger = log.getLogger(LOG_NAME)
try:
    from common.datasource.connection import MYSQL
except Exception as e:
    logger.error("error to import the database class MYSQL | %s", e)
    exit(1)

# QUERY REGIONS

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
        return False

    if MYSQL.result:
        return MYSQL.result

    return False

def consult_region_byid_and_country(id_region, id_country):
    '''
        Retorna o estado (region) por id e país.
    '''
    params = {
        'id': id_region,
        'country_id': id_country
    }

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
            AND id = :id;
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult countries in databases")
        return False

    if MYSQL.result:
        return {
            'id': MYSQL.result[0]['id'],
            'name': MYSQL.result[0]['name'],
            'code': MYSQL.result[0]['code'],
            'default_timezone': MYSQL.result[0]['default_timezone'],
            'country_id': MYSQL.result[0]['country_id']
        }

    return False

def consult_region_byid(id_region):
    '''
        Retorna o estado (region) por id e país.
    '''
    params = {
        'id': id_region
    }

    query = """
        SELECT 
            id,
            name,
            code,
            default_timezone,
            country_id
        FROM `region`
         WHERE
             id = :id;
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult countries in databases")
        return False

    if MYSQL.result:
        return {
            'id': MYSQL.result[0]['id'],
            'name': MYSQL.result[0]['name'],
            'code': MYSQL.result[0]['code'],
            'default_timezone': MYSQL.result[0]['default_timezone'],
            'country_id': MYSQL.result[0]['country_id']
        }

    return False

def create_region(parameters):
    '''

    '''
    params = {
        'name': parameters['name'],
        'code': parameters['code'],
        'default_timezone': parameters['default_timezone'],
        'country_id': parameters['country_id']
    }

    query = """
        INSERT INTO `region`(
                name, 
                code,
                default_timezone,
                country_id
            )
	    VALUES(
            :name,
            :code,
            :default_timezone,
            :country_id
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
        logger.exception("error to create region")
        return False

    logger.info("region created with successfully!")
    return True

def update_region(parameters):
    '''

    '''
    params = {
        'id': parameters['id'],
        'name': parameters['name'],
        'code': parameters['code'],
        'default_timezone': parameters['default_timezone'],
        'country_id': parameters['country_id']
    }

    query = 'UPDATE `region` SET `name` = :name, \
                `code` = :code, \
                `default_timezone` = :default_timezone, \
                `country_id` = :country_id \
            WHERE id = :id'
    
    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to update region")
        return False

    logger.info("region updated with successfully!")
    return True