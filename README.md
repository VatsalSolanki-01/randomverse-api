# RandomVerse CI/CD Pipeline Project

A hands-on DevOps project focused on Docker containerization, Jenkins CI/CD automation, Docker Hub image management, and automated Railway deployment.

---

# What This Project Does

This project demonstrates an end to end CI/CD workflow for containerized applications using Jenkins Pipelines and Docker.

The pipeline automatically:

* Pulls source code from GitHub
* Builds Docker images
* Pushes images to Docker Hub
* Deploys containers to Railway

The Flask application acts as a lightweight deployment workload while the primary focus of the project is CI/CD automation and deployment workflows.

---

# How It Helps / Problems It Solves

Manual deployments are slow and inconsistent.

This project demonstrates how CI/CD pipelines improve deployment automation through:

* Automated Docker image builds
* Continuous integration using Jenkins
* Centralized image management with Docker Hub
* Automated cloud deployment using Railway
* Faster and repeatable deployments
* Consistent runtime environments through containers

---

# CI/CD Architecture

```text id="p5jq6w"
               Developer Pushes Code
                          |
                          v
                     GitHub Repository
                          |
                          v
                   Jenkins Pipeline
                          |
                          v
                 Docker Image Build
                          |
                          v
                   Docker Hub Push
                          |
                          v
                  Railway Deployment
                          |
                          v
                    Running Container
```

---

# Pipeline Workflow

```text id="xkm18w"
GitHub Push
      ↓
Jenkins Trigger
      ↓
Docker Build
      ↓
Docker Hub Push
      ↓
Railway Deployment
```

---

# Tech Stack

| Tool       | Logo                                                                                                           |
| ---------- | -------------------------------------------------------------------------------------------------------------- |
| Docker     | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="40"/>          |
| Jenkins    | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="40"/>        |
| Docker Hub | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="40"/>          |
| Railway    | <img src="https://railway.app/brand/logo-light.png" width="40"/>                                               |
| Python     | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/>          |
| Flask      | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40"/>            |
| Linux      | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="40"/>            |
| GitHub     | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg" width="70"/> |

---

# Jenkins Pipeline Responsibilities

The Jenkins pipeline automates:

* Source code retrieval from GitHub
* Docker image creation
* Docker Hub authentication
* Container image publishing
* Automated Railway deployment

This creates a repeatable and automated deployment workflow.

---

check it out: https://randomverse-api-production.up.railway.app/
