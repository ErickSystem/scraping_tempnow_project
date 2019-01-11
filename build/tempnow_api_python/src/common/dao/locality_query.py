from lib_formatter_logger import log
from config import LOG_NAME
logger = log.getLogger(LOG_NAME)
try:
    from common.datasource.connection import MYSQL
except Exception as e:
    logger.error("error to import the database class MYSQL | %s", e)
    exit(1)

# QUERY LOCALITY

def get_all_localities(region_id):
    """Retorna todas cidades por estado"""

    params = {'region_id': region_id}
    query = """
        SELECT 
            id,
            name,
            region_id
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
        return False

    if MYSQL.result:
        return MYSQL.result

    return False

def consult_locality_byid(locality_id):
    """Retorna a cidade por estado"""

    params = {
        'id': locality_id
    }
    
    query = """
        SELECT 
            id,
            name,
            region_id
        FROM `locality`
        WHERE
            id = :id;
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult locality in databases")
        return False

    if MYSQL.result:
        return {
            'id': MYSQL.result[0]['id'],
            'name': MYSQL.result[0]['name'],
            'region_id': MYSQL.result[0]['region_id']
        }

    return False

def consult_locality_byname(name, region_id):
    """Retorna a cidade por estado consultado por nome e region id"""

    params = {
        'name': str(name).lower(),
        'region_id': region_id
    }
    
    query = """
        SELECT 
            id,
            name,
            region_id
        FROM `locality`
        WHERE
            region_id = :region_id
            AND lower(name) like :name
        ORDER BY
		    id desc;
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult locality in databases")
        return False

    if MYSQL.result:
        return {
            'id': MYSQL.result[0]['id'],
            'name': MYSQL.result[0]['name'],
            'region_id': MYSQL.result[0]['region_id']
        }

    return False

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

def update_locality(parameters):
    '''

    '''
    params = {
        'id': parameters['id'],
        'name': parameters['name'],
        'region_id': parameters['region_id']
    }

    query = 'UPDATE `locality` SET `name` = :name, `region_id` = :region_id WHERE id = :id'

    logger.debug("updating locality...")
    try:
        MYSQL.execute(
            query=query,
            params=params,
            get_results=False,
            check_for_empty_result=False
        )
    except:
        logger.exception("error to update locality")
        return False

    return True