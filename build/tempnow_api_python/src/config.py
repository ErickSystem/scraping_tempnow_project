from lib_formatter_logger import log
from lib_formatter_logger.utils import config_validator

LOG_NAME='tempnow_api_python'

logger = log.getLogger(LOG_NAME)

variables = [
    { "name": "MYSQL_DATABASE_SERVER", "required": True },
    { "name": "MYSQL_DATABASE_PORT", "default": 3306, "type": "int" },
    { "name": "MYSQL_DATABASE_USERNAME", "required": True },
    { "name": "MYSQL_DATABASE_PASSWORD", "required": True },
    { "name": "MYSQL_DATABASE_DATABASE", "required": True },
]

try:
    ( # pylint: disable=E0632
      MYSQL_DATABASE_SERVER
    , MYSQL_DATABASE_PORT
    , MYSQL_DATABASE_USERNAME
    , MYSQL_DATABASE_PASSWORD
    , MYSQL_DATABASE_DATABASE
    ) = config_validator(variables)
except:
    logger.exception("Can't continue due to error in configuration")
    exit(1)

MYSQL_DATABASE_CONN = {
    'drivername': 'mysql+pymysql',
    'host': MYSQL_DATABASE_SERVER,
    'port': MYSQL_DATABASE_PORT,
    'username': MYSQL_DATABASE_USERNAME,
    'password': MYSQL_DATABASE_PASSWORD,
    'database': MYSQL_DATABASE_DATABASE
}


