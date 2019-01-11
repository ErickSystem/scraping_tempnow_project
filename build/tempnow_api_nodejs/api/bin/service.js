// enables ES6 support
//require('newrelic');
require('babel-core/register');

require(['prod', 'dev'].indexOf(process.env.NODE_ENV) > -1 ? '../lib' : '../src').start(require('../config').default);
