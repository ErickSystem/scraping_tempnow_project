import mysql from 'mysql'
import config from '../../config/env'

const connection = mysql.createConnection({
    host     : config.mysql_db.server,
    port     : config.mysql_db.port,
    user     : config.mysql_db.username,
    password : config.mysql_db.password,
    database : config.mysql_db.db
    
});

module.exports = connection;