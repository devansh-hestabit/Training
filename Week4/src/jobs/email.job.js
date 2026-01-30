const { Queue } = require('bullmq');
const redisConnection = require('../config/redis');

const emailQueue = new Queue('email-queue', {
  connection: redisConnection,
  defaultJobOptions: {
    attempts: 3,           // retry 3 times
    backoff: {
      type: 'exponential',
      delay: 5000,         // 5 seconds
    },
    removeOnComplete: true,
    removeOnFail: false,
  },
});

async function addEmailJob(data) {
  await emailQueue.add('send-email', data);
}

module.exports = {
  emailQueue,
  addEmailJob,
};
