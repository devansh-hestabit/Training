#!/bin/bash
docker compose -f docker-compose.prod.yml down
docker build -t travel-backend ./server
docker build -t travel-frontend ./client
docker compose -f docker-compose.prod.yml up -d


