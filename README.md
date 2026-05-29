# End-to-End Automated Cloud-Native Lab 

A comprehensive, full-stack automation project that transforms bare-metal/virtualized environments into a self-healing, CI/CD-driven Kubernetes ecosystem.

## Architecture Overview
The lab follows a layered approach to infrastructure:
1.  **Hypervisor Layer:** KVM-based virtualization on Linux.
2.  **IaC Layer:** Ansible playbooks for automated VM provisioning and OS hardening.
3.  **Orchestration Layer:** Kubernetes (K3s/Kubeadm) managing containerized microservices.
4.  **CI/CD Layer:** Jenkins pipelines automating builds from Git to Registry.
5.  **Observability Layer:** Prometheus, Grafana, and custom Python/Bash health-check scripts.

---

## Tech Stack
* **Virtualization:** KVM, Libvirt, QEMU
* **Infrastructure as Code:** Ansible
* **Orchestration:** Kubernetes (K8s), Docker
* **CI/CD:** Jenkins, Git
* **Monitoring:** Grafana, Prometheus
* **Scripting:** Python 3, Bash

---

## Key Features

### 1. Infrastructure Automation (Ansible)
* **Zero-Touch Provisioning:** Ansible playbooks automate the creation of KVM virtual machines, including CPU/RAM allocation, network bridging, and SSH key injection.
* **Configuration Consistency:** Ensures all nodes (Master/Workers) have identical dependencies, reducing "it works on my machine" issues.

### 2. CI/CD Pipeline (Jenkins)
* **Automated Builds:** Jenkins triggers on Git commits to build Docker images.
* **Testing:** Integrated automated testing phase to validate images before deployment.
* **Fast Deployment:** Reduced deployment time by over 60% through automated image tagging and rolling updates in K8s.

### 3. Container Orchestration (Kubernetes)
* **Microservices:** Deployment of containerized applications using standard YAML manifests.
* **Scalability:** Configured horizontal pod autoscaling and service discovery.

### 4. Automated Health Checks & Log Analysis
* **Python Scripts:** Custom scripts that query the K8s API to identify and report `CrashLoopBackOff` or `Pending` pods.
* **Bash Tooling:** Automated log rotation and keyword-based error scanning (Regex) for rapid root cause analysis.

### 5. Real-time Monitoring (Grafana)
* Visualized node metrics (CPU, Memory, Disk I/O) and container health status.
* Custom alerting thresholds for proactive system maintenance.

---

## Project Structure
```
├── ansible/            # Playbooks for VM and K8s setup
├── cicd/               # Jenkinsfile and build configurations
├── k8s-manifests/      # Deployment, Service, and Ingress files
├── scripts/            # Python health checks & Bash log analyzers
└── app/                # Sample microservice source code
```
