import express from 'express';
import morgan from 'morgan';
import logger from './util/logger';
var cors = require("cors");

// Settings
export async function start (config) {
    try {
      // Setting
      const app = express();
      
      app.set('config', config);
      app.set('json spaces', 4);
      app.use(morgan('dev'));
      app.use(express.json());
  
      app.use((err, req, res, next) => {
          logger.error(err.stack || err);
      });

      app.use(function(req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
      });
      
      app.options('*', cors()); 
  
      // Starting the server
      app.listen(config.env.http.port, config.env.http.host, () => {
        logger.info(`Servidor iniciado em [ http://${config.env.http.host}:${config.env.http.port} ]`);
      });
  
      // Routes
      app.use('/api', require('./routes/wf.routes'));
  
    } catch (err) {
      logger.error(err.stack || err);
    }
  }

