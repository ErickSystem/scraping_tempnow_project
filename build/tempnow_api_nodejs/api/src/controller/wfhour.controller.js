import logger from '../util/logger'
import conn from '../datasource/connection'

const ctl = {};

ctl.getAllWfHours = async (req, res) => {
    logger.info('route list weather forecasting hour')
    const { locality_id } = req.params;
    var queryString = "SELECT wf.id,wf.atmospheric_pressure,wf.wind,wf.temp,wf.relative_humidity,wf.last_update,wf.weather,"
            + " wf.locality_id,wf.date_time,l.`name` as locality_name,r.`name` as region_name,r.`code`"
            + " FROM `weather_forecasting_hour` wf"
            + " JOIN locality l ON l.id = wf.locality_id"
            + " JOIN region r ON r.id = l.region_id"
            + " WHERE l.id =" + locality_id
            + " ORDER BY wf.date_time;"
    logger.info(queryString)
    conn.query(queryString, function(err, result){
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'nothing data to list in database'
            }).end();
        else
            res.json({
                success: true,
                wfhours: result
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
};

ctl.getWfHour = async (req, res) => {
    logger.info('route get only one weather forecasting hour')
    const { id } = req.params;
    conn.query('SELECT * FROM weather_forecasting_hour WHERE id=' + id, function(err, result){
        logger.info(err, result)
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'weather forecasting hour id ' + String(id) + ' not found in database'
            }).end();
        else
            res.json({
                success: true,
                wfhour: result[0]
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
};

ctl.createWfHour = async (req, res) => {
    /*
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
    */

    logger.info('route create weather forecasting hour')

    const queryString = `INSERT INTO weather_forecasting_hour(atmospheric_pressure, `
            + ` wind, temp, relative_humidity, weather, locality_id, date_time)`
            + ` VALUES(${req.body.atmospheric_pressure}, ${req.body.wind}, ${req.body.temp},`
            + ` ${req.body.relative_humidity}, '${req.body.weather}',`
            + ` ${req.body.locality_id}, '${req.body.date_time}');`;

    logger.info(queryString)
    conn.query(queryString, function(err, result){
        logger.info(err, result)
        res.json({
            success: true,
            message: 'created with succesfully'
        }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error to create'
        });
    });
};

ctl.updateWfHour = async (req, res) => {
    /*
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
    */
   
    logger.info('route update weather forecasting hour')
    const { id } = req.params;
    const queryString = `UPDATE weather_forecasting_hour SET atmospheric_pressure = ${req.body.atmospheric_pressure},`
            + ` wind = ${req.body.wind}, temp = ${req.body.temp}, relative_humidity = ${req.body.relative_humidity},`
            + ` weather = '${req.body.weather}',`
            + ` locality_id = ${req.body.locality_id}, date_time = '${req.body.date_time}'`
            + ` WHERE id = ${id};`;

    logger.info(queryString)
    conn.query(queryString, function(err, result){
        logger.info(err, result)
        res.json({
            success: true,
            message: 'updated with succesfully'
        }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error to update'
        });
    });
};

ctl.deleteWfHour = async (req, res) => {
    logger.info('route delete weather forecasting hour')
    const { id } = req.params;
    const queryString = `DELETE FROM weather_forecasting_hour WHERE id = ${id}`

    logger.info(queryString)
    conn.query(queryString, function(err, result){
        logger.info(err, result)
        res.json({
            success: true,
            message: 'deleted with succesfully'
        }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error to delete'
        });
    });
};

module.exports = ctl;