import logger from '../util/logger'
import conn from '../datasource/connection'

const ctl = {};

ctl.getAllCountries = async (req, res) => {
    logger.info('route list countries')
    conn.query('SELECT * FROM country', function(err, result){
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'nothing data to list in database'
            }).end();
        else
            res.json({
                success: true,
                countries: result
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
};

ctl.getCountry = async (req, res) => {
    logger.info('route get only one country')
    const { id } = req.params;
    conn.query('SELECT * FROM country WHERE id=' + id, function(err, result){
        logger.debug(err, result)
        if (result.length <= 0)
            res.json({
                success: false,
                message: 'country id ' + String(id) + ' not found in database'
            }).end();
        else
            res.json({
                success: true,
                country: result[0]
            }).end();
    }).on('error', function(err) {
        logger.error("[mysql error]", err);
        res.json({
            success: false,
            message: 'error tor list'
        });
    });
 
};

module.exports = ctl;