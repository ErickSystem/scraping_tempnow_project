from lib_connection_sqldb import sqldb
from config import (
    MYSQL_DATABASE_CONN
)

MYSQL = sqldb.MySQL(conn=MYSQL_DATABASE_CONN)

def return_conn_tran():
    """
        Retorna uma tupla com:
        - Transaction
        - Connection
    """
    trans, conn = MYSQL.open_session()
    return  trans, conn
