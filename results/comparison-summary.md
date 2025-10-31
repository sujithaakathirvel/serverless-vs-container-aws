# 🧾 Comparison Summary — Serverless vs Container on AWS

This summary highlights the key outcomes from testing and analysing both versions of the To-Do API.

---

## ⚙️ Architectures Compared

| Architecture | Stack | Description |
|---------------|--------|-------------|
| **Serverless** | AWS Lambda, API Gateway, DynamoDB | Event-driven and fully managed. No servers to maintain. Auto-scales based on request load. |
| **Container-based** | Flask, Docker, ECS Fargate | Flask API containerised and deployed on ECS using Fargate tasks. More control over configuration and scaling behaviour. |

---

## 📊 Performance Observations

| Metric | Serverless (Lambda) | Container (ECS Fargate) |
|--------|----------------------|--------------------------|
| **Average Response Time** | Slightly higher due to cold starts during idle periods | Consistent, lower latency at steady load |
| **Scalability** | Auto-scales instantly under burst traffic | Scales predictably once thresholds are configured |
| **Throughput (JMeter)** | Occasional throttling during heavy bursts | Stable performance with 0% errors |
| **Error Rate** | ~2–3% during peak load tests | 0% errors recorded in load tests |
| **Deployment Speed** | Faster (no instance provisioning) | Slower initial setup due to container build and task definition |
| **Monitoring** | Integrated with CloudWatch Logs and X-Ray | Requires custom metrics and log drivers |
| **Cost** | Lower for low/variable workloads | Higher baseline cost due to idle Fargate task time |

---

## 💡 Insights

- **Serverless** is ideal for lightweight, unpredictable, or spiky workloads.  
  It’s quick to deploy and cost-efficient when not constantly active.  

- **Containers** are better suited for consistent, long-running workloads.  
  They offer better control and predictable performance but add management overhead.

---

## 🧠 Conclusion

Both architectures successfully implemented the same To-Do API,  
but they serve different needs:

- For **rapid scaling, minimal ops, and cost efficiency → Serverless wins.**  
- For **predictable throughput, stable latency, and configurable environments → Containers win.**

> In production, a **hybrid approach**—combining serverless APIs with containerised microservices—often delivers the best balance of cost and control.

---

**Author:** Sujithaa Kathirvel  
**Course:** MSc Computing @ University of East London  
**Project:** Comparative Study of Serverless vs Container-based Cloud Architecture on AWS
