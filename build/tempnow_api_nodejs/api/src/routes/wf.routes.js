import express from 'express';
const router = express.Router();

const countryCtl = require('../controller/country.controller');
const regionCtl = require('../controller/region.controller');
const localityCtl = require('../controller/locality.controller');
const wfhouryCtl = require('../controller/wfhour.controller');
const wfdayCtl = require('../controller/wfday.controller');

/* ROUTES COUNTRY */
router.get('/countries', countryCtl.getAllCountries);
router.get('/countries/:id', countryCtl.getCountry);

/* ROUTES REGION */
router.get('/regions/:country_id', regionCtl.getAllRegions);
router.get('/regions/:id/region', regionCtl.getRegion);
router.post('/regions', regionCtl.createRegion);
router.put('/regions/:id/region', regionCtl.updateRegion);
router.delete('/regions/:id/region', regionCtl.deleteRegion);

/* ROUTES LOCALITY */
router.get('/localities/:region_id', localityCtl.getAllLocalities);
router.get('/localities/:locality_id/locality', localityCtl.getLocality);
router.post('/localities', localityCtl.createLocality);
router.put('/localities/:locality_id/locality', localityCtl.updateLocality);
router.delete('/localities/:locality_id/locality', localityCtl.deleteLocality);

/* ROUTES WEATHER FORECASTING HOUR */
router.get('/wfhours/:locality_id', wfhouryCtl.getAllWfHours);
router.get('/wfhours/:id/wfhour', wfhouryCtl.getWfHour);
router.post('/wfhours', wfhouryCtl.createWfHour);
router.put('/wfhours/:id/wfhour', wfhouryCtl.updateWfHour);
router.delete('/wfhours/:id/wfhour', wfhouryCtl.deleteWfHour);

/* ROUTES WEATHER FORECASTING DAY */
router.get('/wfdays/:locality_id', wfdayCtl.getAllWfDays);
router.get('/wfdays/:id/wfday', wfdayCtl.getWfDay);
router.post('/wfdays', wfdayCtl.createWfDay);
router.put('/wfdays/:id/wfday', wfdayCtl.updateWfDay);
router.delete('/wfdays/:id/wfday', wfdayCtl.deleteWfDay);


module.exports = router;