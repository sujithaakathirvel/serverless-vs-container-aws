# Serverless vs Container on AWS — To-Do App (My MSc Computing Project)
![Verify](https://github.com/sujithaakathirvel/serverless-vs-container-aws/actions/workflows/verify.yml/badge.svg)

This is my MSc Computing dissertation project where I built the same **To-Do API** using two different AWS architectures:
- **Serverless:** AWS Lambda + API Gateway + DynamoDB  
- **Containerised:** Flask + Docker + ECS Fargate  

The aim was to compare both in terms of **performance, scalability, cost, and deployment complexity** with real test results.

---

## 🧩 Project Structure

- **/serverless-version** → The To-Do API built using AWS Lambda, API Gateway, and DynamoDB (via AWS SAM).  
- **/container-version** → The same API built with Flask, containerised using Docker, and deployed on ECS Fargate.  
- **/docs** → All screenshots and validation proofs from AWS (Lambda, ECS, DynamoDB, JMeter).  
- **/results** → Summary and comparison notes from the dissertation.

---

## ☁️ Summary of Findings
- **Serverless:** Auto-scales, lower cost for variable traffic, minimal maintenance.  
- **Container:** More stable under sustained load, consistent latency, slightly higher idle cost.

Full notes → [/results/comparison-summary.md](results/comparison-summary.md)

---

## 📸 Proof of Deployment
All AWS and testing screenshots are organised inside the **/docs** folder:
- `docs/serverless/` → Lambda, API Gateway, DynamoDB proofs  
- `docs/container/` → ECS Fargate & Flask app proofs  
- `docs/jmeter/` → Load-testing results comparing both architectures

---

## 🧠 Technologies Used
AWS Lambda · API Gateway · DynamoDB · ECS Fargate · Docker · Flask · Python · CloudWatch · JMeter

---

## 📜 License
MIT
