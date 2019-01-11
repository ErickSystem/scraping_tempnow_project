from lib_formatter_logger import log
from config import LOG_NAME
logger = log.getLogger(LOG_NAME)
try:
    from common.datasource.connection import MYSQL
except Exception as e:
    logger.error("error to import the database class MYSQL | %s", e)
    exit(1)

def get_all_country():
    """Return all countries"""

    query = """
        SELECT 
            *
        FROM `country`;
    """
    try:
        MYSQL.execute(
            query=query,
            params=None
        )
    except:
        logger.exception("error to consult country in databases")
        return False

    if MYSQL.result:
        return MYSQL.result

    logger.warning('failed consult all countries')
    return False

def get_country_byid(country_id):
    """Return all countries"""
    params = {
        'id': country_id
    }

    query = """
        SELECT 
            *
        FROM `country`
        WHERE
            id = :id
    """
    try:
        MYSQL.execute(
            query=query,
            params=params
        )
    except:
        logger.exception("error to consult country by id in databases")
        return False

    if MYSQL.result:
        return MYSQL.result

    logger.warning('failed consult country by id')
    return False