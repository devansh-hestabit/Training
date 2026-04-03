const express = require('express');
const routes = require('../routes');
const logger = require('../utils/logger');
const errorMiddleware = require('../middlewares/error.middleware');
const securityMiddleware = require('../middlewares/security');
const tracing = require('../utils/tracing');



module.exports = function loadApp() {
  const app = express();
  const tracing = require('../utils/tracing');
  app.use(express.urlencoded({ extended: true }));
  securityMiddleware(app);
  logger.info('Middlewares loaded');

  app.use('/api', routes);
  logger.info('Routes mounted: 1 endpoint');

  app.use(errorMiddleware);

  return app;
};
