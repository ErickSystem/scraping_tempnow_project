import logger from '../util/logger'
import conn from '../datasource/connection'

const ctl = {};

ctl.getAllWfDays = async (req, res) => {
    logger.info('route list weather forecasting day')
    const { locality_id } = req.params;
    var queryString = "SELECT wf.id, wf.weather, wf.precipitation, wf.`date`, wf.`max`, wf.`min`,"
                + " wf.locality_id, wf.lag, l.`name` as locality_name, r.`name` as region_name, r.`code`"
                + " FROM `weather_forecasting_day` wf"
                + " JOIN locality l ON l.id = wf.locality_id"
                + " JOIN region r ON r.id = l.region_id"
                + " WHERE l.id=" + locality_id
                + " ORDER BY wf.`date`;"
    console.log(queryString)
    conn.query(queryString, function(err, result){
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'nothing data to list in database'
            }).end();
        else
            res.json({
                success: true,
                wfdays: result
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
};

ctl.getWfDay = async (req, res) => {
    logger.info('route get only one weather forecasting day ')
    const { id } = req.params;
    conn.query('SELECT * FROM weather_forecasting_day WHERE id=' + id, function(err, result){
        logger.info(err, result)
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'weather forecasting day id ' + String(id) + ' not found in database'
            }).end();
        else
            res.json({
                success: true,
                wfday: result[0]
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
};

ctl.createWfDay = async (req, res) => {
    /*
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
   
    */

    logger.info('route create weather forecasting hour')

    const queryString = `INSERT INTO weather_forecasting_day(weather,`
            + ` precipitation, date, max, min, locality_id, lag)`
            + ` VALUES('${req.body.weather}', ${req.body.precipitation}, '${req.body.date}', `
            + ` ${req.body.max}, ${req.body.min}, `
            + ` ${req.body.locality_id}, ${req.body.lag});`;

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

ctl.updateWfDay = async (req, res) => {
    /*
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
   
    */
    logger.info('route update weather forecasting hour')
    const { id } = req.params;
    const queryString = `UPDATE weather_forecasting_day SET weather = '${req.body.weather}', `
            + ` precipitation = ${req.body.precipitation}, date = '${req.body.date}', max = ${req.body.max},`
            + ` min = ${req.body.min}, locality_id = ${req.body.locality_id}`
            + ` WHERE id = ${id}`;

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

ctl.deleteWfDay = async (req, res) => {
    logger.info('route delete weather forecasting day')
    const { id } = req.params;
    const queryString = `DELETE FROM weather_forecasting_day WHERE id = ${id}`

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