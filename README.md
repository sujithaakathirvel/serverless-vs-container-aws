# Serverless vs Container on AWS — To-Do App Comparison

This repo contains **two implementations** of the same To-Do API from my MSc dissertation:
- **Serverless version**: AWS Lambda + API Gateway + DynamoDB
- **Container version**: Flask + Docker + ECS Fargate

The goal is to compare **performance, cost, ease of deployment, and security** with a real app.

## Repo Structure
/serverless-version # Lambda + API GW + DynamoDB (SAM)
/container-version # Flask API containerized and deployed on ECS Fargate
/docs # diagrams, screenshots, charts

## Quick Start
- **Serverless** → see `/serverless-version/README.md`
- **Container** → see `/container-version/README.md`

## High-level Findings (from my dissertation)
- **Serverless**: Auto-scales quickly and is cost-efficient at low/variable traffic, but can show higher error rates under extreme bursts.
- **Containers**: Stable performance with 0% errors in my tests; predictable at sustained load; higher base cost when idle.

> Full write-up and charts will be added in `/docs`.

## License
MIT
