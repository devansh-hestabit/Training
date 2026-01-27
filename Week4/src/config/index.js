const dotenv = require('dotenv');
const path = require('path');

const env = process.env.NODE_ENV || 'local';

dotenv.config({
  path: path.resolve(process.cwd(), `.env.${env}`)
});

module.exports = {
  env,
  port: process.env.PORT,
  mongoUri: process.env.MONGO_URI,
  logLevel: process.env.LOG_LEVEL
};
