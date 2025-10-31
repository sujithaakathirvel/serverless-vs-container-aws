# Serverless vs Container on AWS — To-Do App Comparison

This project contains **two implementations** of the same To-Do API from my MSc Computing dissertation:

- **Serverless version**: AWS Lambda + API Gateway + DynamoDB  
- **Container version**: Flask + Docker + ECS Fargate  

The goal is to compare **performance, cost, ease of deployment, and security** using real workloads.

---

## Repo Structure
/serverless-version → Lambda + API Gateway + DynamoDB (SAM)  
/container-version → Flask API containerized and deployed on ECS Fargate  
/docs → Architecture diagram, screenshots, metrics

---

## Proof of Deployment

**Serverless (Lambda)**  
![Lambda metrics](docs/serverless/lambda-metrics.png.png)  
![API proof](docs/serverless/api.png.png)  
![DynamoDB table](docs/serverless/DynamoDB.png)   
![JMeter load test results (Serverless)](docs/serverless/serverless.png.png)

**Container (ECS)**  
![ECS service](docs/container/ecs-service.png.png)  
![Flask app running](docs/container/flask-api-proof.png.png)  
![ECS metrics](docs/container/ecs-metrics.png.png)  
![JMeter results](docs/container/ecs-jmeter-results.png.png)
---

## License
MIT
