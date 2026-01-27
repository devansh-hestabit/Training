const loadApp = require('./loaders/app');
const loadDB = require('./loaders/db');
const config = require('./config');
const logger = require('./utils/logger');

async function startServer() {
  try {
    const app = loadApp();

    await loadDB();

    app.listen(config.port, () => {
      logger.info(`Server started on port ${config.port}`);
    });
  } catch (error) {
    logger.error('Application failed to start');
    process.exit(1);
  }
}

startServer();
