const { Worker } = require('bullmq');
const redisConnection = require('../config/redis');
const logger = require('../utils/logger');

const worker = new Worker(
  'email-queue',
  async (job) => {
    logger.info('Processing email job', {
      jobId: job.id,
      requestId: job.data.requestId,
    });

    await new Promise((resolve) => setTimeout(resolve, 2000));

    logger.info('Email sent successfully', {
      to: job.data.to,
      requestId: job.data.requestId,
    });
  },
  { connection: redisConnection }
);

worker.on('failed', (job, err) => {
  logger.error('Email job failed', {
    jobId: job.id,
    error: err.message,
  });
});

console.log('📨 Email worker started');
