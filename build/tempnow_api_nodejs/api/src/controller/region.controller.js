import logger from '../util/logger'
import conn from '../datasource/connection'

const ctl = {};

ctl.getAllRegions = async (req, res) => {
    logger.info('route list regions')
    const { country_id } = req.params;
    conn.query('SELECT * FROM region WHERE country_id=' + country_id , function(err, result){
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'nothing data to list in database'
            }).end();
        else
            res.json({
                success: true,
                regions: result
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error to list'
        });
    });
};

ctl.getRegion = async (req, res) => {
    logger.info('route get only one region')
    const { id } = req.params;
    conn.query('SELECT * FROM region WHERE id=' + id, function(err, result){
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'region id ' + String(id) + ' not found in database'
            }).end();
        else
            res.json({
                success: true,
                region: result[0]
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error to list'
        });
    });
};

ctl.createRegion = async (req, res) => {
    logger.info('route create region')
    const queryString = `INSERT INTO region(name, code, default_timezone, country_id)` 
         + ` VALUES('${req.body.name}', '${req.body.code}', '${req.body.default_timezone}', ${req.body.country_id});`
    logger.info(queryString)
    conn.query(queryString, function(err, result){
        logger.info(err, result)
        res.json({
            success: true,
            message: 'created with successfully!'
        }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error to create'
        });
    });
};
ctl.updateRegion = async (req, res) => {
    logger.info('route update region')
    const { id } = req.params;
    const queryString = `UPDATE region SET name = '${req.body.name}', `
        + ` code = '${req.body.code}', default_timezone = '${req.body.default_timezone}', `
        + ` country_id = ${req.body.country_id}` 
        + ` WHERE id = ${id}`

    logger.info(queryString)
    conn.query(queryString, function(err, result){
        logger.info(err, result)
        res.json({
            success: true,
            message: 'updated with successfully!'
        }).end();
    }).on('error', function(err) {
        logger.info("[mysql error]", err);
        res.json({
            success: false,
            message: 'error to update'
        });
    });
};

ctl.deleteRegion = async (req, res) => {
    logger.info('route delete region')
    const { id } = req.params;
    conn.query('DELETE FROM region WHERE id=' + id, function(err, result){
        logger.info(err, result)
        res.json({
            success: true,
            message: 'deleted with successfully!'
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