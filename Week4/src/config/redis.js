const { Redis } = require('ioredis');

const connection = new Redis({
  host: '127.0.0.1',
  port: 6379,

  // REQUIRED FOR BULLMQ
  maxRetriesPerRequest: null,

  // Recommended
  enableReadyCheck: false,
});

connection.on('connect', () => {
  console.log('✅ Redis connected');
});

connection.on('error', (err) => {
  console.error('❌ Redis error', err);
});

module.exports = connection;
