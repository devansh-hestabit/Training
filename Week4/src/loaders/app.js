const express = require('express');
const routes = require('../routes');
const logger = require('../utils/logger');
const errorMiddleware = require('../middlewares/error.middleware');

module.exports = function loadApp() {
  const app = express();

  app.use(express.json());
  app.use(express.urlencoded({ extended: true }));

  logger.info('Middlewares loaded');

  app.use('/api', routes);
  logger.info('Routes mounted: 1 endpoint');

  app.use(errorMiddleware);

  return app;
};
