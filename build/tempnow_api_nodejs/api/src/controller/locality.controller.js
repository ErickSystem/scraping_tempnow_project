import logger from '../util/logger'
import conn from '../datasource/connection'

const ctl = {};

ctl.getAllLocalities = async (req, res) => {
    logger.info('route list localities')
    const { region_id } = req.params;
    conn.query('SELECT * FROM locality WHERE region_id=' + region_id + ' ORDER BY name;', function(err, result){
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'nothing data to list in database'
            }).end();
        else
            res.json({
                success: true,
                localities: result
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
};

ctl.getLocality = async (req, res) => {
    logger.info('route get only one locality')
    const { locality_id } = req.params;
    conn.query('SELECT * FROM locality WHERE id=' + locality_id, function(err, result){
        logger.info(err, result)
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'locality id ' + String(locality_id) + ' not found in database'
            }).end();
        else
            res.json({
                success: true,
                locality: result[0]
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
};

ctl.createLocality = async (req, res) => {
    logger.info('route create locality')
    const queryString = `INSERT INTO locality(name, region_id)` 
         + ` VALUES('${req.body.name}', ${req.body.region_id});`;
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
ctl.updateLocality = async (req, res) => {
    logger.info('route update locality')
    const { locality_id } = req.params;
    const queryString = `UPDATE locality SET name = '${req.body.name}', ` + ` region_id = ${req.body.region_id} WHERE id = ${locality_id}`;

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

ctl.deleteLocality = async (req, res) => {
    logger.info('route delete region')
    const { locality_id } = req.params;
    conn.query('DELETE FROM locality WHERE id=' + locality_id, function(err, result){
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