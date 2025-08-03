

```markdown
#  AI Anime Recommender System 

A full-stack **AI Anime Recommender System** built using **LangChain, ChromaDB, Kubernetes (Minikube), Grafana Cloud, and Streamlit**.  
It combines semantic search with intelligent recommendations, deployed in a scalable, monitorable MLOps pipeline.

---

##  Features

-  **Semantic Anime Recommendations** using LangChain + Hugging Face Embeddings
-  **Vector Store Retrieval** with ChromaDB
- 🖥 **Streamlit Frontend UI** for interactive inputs
-  **Dockerized Deployment** for portability
- ☸ **Kubernetes + Minikube** for container orchestration
-  **Grafana Cloud Monitoring** for observability and performance insights

---

##  Tech Stack

| Layer         | Tools/Frameworks                                |
|--------------|--------------------------------------------------|
| LLM & RAG     | LangChain, Hugging Face Transformers            |
| Vector Store  | ChromaDB                                         |
| Backend       | Python, Streamlit                               |
| Container     | Docker                                           |
| Orchestration | Kubernetes, Minikube                            |
| Monitoring    | Grafana Cloud, Prometheus, Node Exporter        |

---
##  Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PrinceGupta8/AI-Anime-Recommender-using-Grafana-Cloud-Minikube-ChromaDB-Langchain.git
cd AI-Anime-Recommender-using-Grafana-Cloud-Minikube-ChromaDB-Langchain
````

### 2️⃣ Set Up Python Environment

```bash
python -m venv animeenv
source animeenv/bin/activate  # For Windows: animeenv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Prepare .env File

Create a `.env` file in the root and add:

```env
HUGGINGFACEHUB_API_TOKEN=your_token
```

---

##  Dockerize the App

### Build & Run Locally

```bash
docker build -t anime-recommender .
docker run -p 8501:8501 anime-recommender
```

---

## ☸ Kubernetes Deployment

### Start Minikube

```bash
minikube start
```

### Apply Kubernetes Manifest

```bash
kubectl apply -f k8s/llmops-k8s.yaml
kubectl get pods
```

### Access App

```bash
minikube service llmops-service
```

---

## Grafana Cloud Integration

1. Sign up at [Grafana Cloud](https://grafana.com)
2. Install Prometheus and Node Exporter on Minikube
3. Configure Prometheus data source in Grafana Cloud
4. Use default dashboards or build custom ones to monitor:

   * CPU, Memory, Disk usage
   * Pod status
   * App response time

---



## 📬 Connect with Me

*  [LinkedIn](https://www.linkedin.com/in/prince-gupta-a8129a209/)
*  Email: [princegupta995643@gmail.com](mailto:princegupta995643@gmail.com)



