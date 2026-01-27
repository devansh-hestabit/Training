const winston = require('winston');
const { logLevel } = require('../config');

const logger = winston.createLogger({
  level: logLevel || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.printf(
      ({ level, message, timestamp }) =>
        `${timestamp} [${level.toUpperCase()}]: ${message}`
    )
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'src/logs/app.log' })
  ]
});

module.exports = logger;
