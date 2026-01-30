#  Deployment Notes — Week 4 Backend Project

This document describes how to deploy and run the backend application in a
production-ready environment.

##  Tech Stack

- Node.js
- Express
- MongoDB
- Redis
- BullMQ (Background Jobs)
- PM2 (Process Manager)

##  Application Components

The backend consists of **two independent processes**:

### 1 API Server
- Handles incoming HTTP requests
- Exposes REST APIs
- Pushes background jobs to Redis queues

### 2 Worker Process
- Runs independently from the API
- Consumes jobs from BullMQ queues
- Handles async tasks such as email notifications

## Environment Configuration

All environment variables must be defined in a `.env` file.

A reference file is provided:

```
.env.example
```
### Required Environment Variables

```env
NODE_ENV=production
PORT=4000
DATABASE_URL=mongodb://localhost:27017/week4
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```
## Logging Strategy

- Structured logging is implemented using **Pino**
- Each log entry includes:
  - Timestamp
  - Log level
  - Request ID (`X-Request-ID`)
- Logs are written to **stdout**
- In production, logs are managed by **PM2**

This allows:
- Easy debugging
- Request-level traceability
- Integration with monitoring tools

##  Request Tracing

- Every incoming request is assigned a unique `X-Request-ID`
- The same ID is propagated across:
  - Controllers
  - Services
  - Background jobs
  - Logs

This enables full request tracing across the system.

## 🧪 Pre-Deployment Checklist

Before deploying, ensure:

-  MongoDB is running
- Redis is running
- `.env` file is configured
- Postman collection is validated
- Worker process is included in PM2 config