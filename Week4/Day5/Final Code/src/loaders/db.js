const mongoose = require('mongoose');
const { mongoUri } = require('../config');
const logger = require('../utils/logger');

module.exports = async function loadDB() {
  try {
    await mongoose.connect(mongoUri);
    logger.info('Database connected');
  } catch (error) {
    logger.error('Database connection failed');
    throw error;
  }
};
