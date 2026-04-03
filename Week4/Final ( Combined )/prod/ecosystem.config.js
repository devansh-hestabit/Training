module.exports = {
  apps: [
    {
      name: 'week4-api',
      script: 'src/index.js',
      instances: 1,
      autorestart: true,
      env: {
        NODE_ENV: 'production',
      },
    },
    {
      name: 'email-worker',
      script: 'src/jobs/email.worker.js',
      instances: 1,
      autorestart: true,
    },
  ],
};
