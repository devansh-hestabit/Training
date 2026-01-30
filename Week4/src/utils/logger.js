const pino = require('pino');

const logger = pino({
  level: 'info',
  timestamp: () => `,"time":"${new Date().toISOString()}"`,
});

module.exports = {
  info: (msg, meta = {}) => logger.info(meta, msg),
  error: (msg, meta = {}) => logger.error(meta, msg),
};
