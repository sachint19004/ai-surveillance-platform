# 🛡️ AI Surveillance Platform

> A modular AI-powered surveillance platform built with **FastAPI**, **PostgreSQL**, and **Docker**, designed for real-time face recognition, person detection, event monitoring, and security analytics.

> **🚧 Project Status:** Active Development

---

## 📖 Overview

The AI Surveillance Platform is a full-stack intelligent surveillance system designed to demonstrate modern software engineering practices combined with computer vision and AI.

The platform aims to provide:

- Real-time person detection
- Face recognition
- Camera management
- Event logging
- Security alerts
- Analytics dashboard
- REST APIs
- Dockerized deployment

This project is being developed with a scalable and modular architecture, making it easy to extend with additional AI models, cloud deployment, and enterprise features.

---

## ✨ Features

### ✅ Completed

- FastAPI backend architecture
- Modular project structure
- PostgreSQL integration
- Dockerized database
- REST API foundation
- Swagger/OpenAPI documentation
- Environment configuration
- Database connectivity
- Health check endpoints

### 🚧 In Progress

- Face Recognition Service
- Person Detection Service
- Event Logging
- Camera Management
- Analytics Module
- Alert System
- Authentication

### 📌 Planned

- React Dashboard
- JWT Authentication
- Multi-camera Support
- Live Video Streaming
- Redis Caching
- Celery Background Tasks
- Email Notifications
- Mobile Alerts
- Kubernetes Deployment
- Cloud Hosting

---

# 🏗 Project Architecture

```
                     React Dashboard
                           │
                           │
                    REST API (FastAPI)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
 Detection Service   Recognition Service   Analytics
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    PostgreSQL Database
                           │
                      Docker Container
```

---

# 📂 Project Structure

```
ai-surveillance-platform/

│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   │   ├── alerts/
│   │   ├── analytics/
│   │   ├── camera/
│   │   ├── detection/
│   │   ├── recognition/
│   │   └── storage/
│   ├── utils/
│   └── main.py
│
├── assets/
│   ├── authorised/
│   ├── uploads/
│   ├── snapshots/
│   └── temp/
│
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Tech Stack

## Backend

- FastAPI
- Python
- SQLAlchemy
- Pydantic
- Uvicorn

## Database

- PostgreSQL

## AI & Computer Vision

- OpenCV
- InsightFace *(Planned)*
- YOLO *(Planned)*

## DevOps

- Docker
- Docker Compose

## Frontend *(Planned)*

- React
- Axios
- Tailwind CSS

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/sachint19004/ai-surveillance-platform.git

cd ai-surveillance-platform
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Create a `.env` file.

Example:

```env
APP_NAME=AI Surveillance Platform
APP_VERSION=1.0.0

DATABASE_URL=postgresql://postgres:password@localhost:5432/ai_surveillance

SECRET_KEY=your-secret-key

DEBUG=True
```

---

## 5. Start PostgreSQL

```bash
docker compose up -d
```

---

## 6. Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

## 7. Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📡 API

Current API modules include:

- Authentication *(Planned)*
- Users
- Camera
- Detection
- Recognition
- Events
- Analytics

Swagger UI is available at:

```
/docs
```

---

# 🗄 Database

Current database includes support for:

- Users
- Authorized Faces
- Cameras
- Events
- Alerts
- Recognition Logs

More tables will be added as the platform evolves.

---

# 🧠 AI Pipeline

```
Camera Feed
      │
      ▼
Person Detection
      │
      ▼
Face Detection
      │
      ▼
Face Recognition
      │
      ▼
Database Matching
      │
      ▼
Event Logging
      │
      ▼
Alert Generation
      │
      ▼
Dashboard
```

---

# 📈 Roadmap

## Phase 1

- [x] Backend Setup
- [x] PostgreSQL
- [x] Docker
- [x] Project Architecture

## Phase 2

- [ ] Detection Service
- [ ] Recognition Service
- [ ] Camera APIs

## Phase 3

- [ ] React Dashboard
- [ ] Authentication
- [ ] Analytics

## Phase 4

- [ ] Deployment
- [ ] CI/CD
- [ ] Kubernetes

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📜 License

This project is currently licensed under the MIT License.

---

# 👨‍💻 Author

**Sachin T**

GitHub:
https://github.com/sachint19004

LinkedIn:
https://www.linkedin.com/in/sachin-taspire19/

---

## ⭐ Support

If you found this project interesting, consider giving it a **⭐ Star** on GitHub.

It helps support the project and motivates further development.

---

> 🚀 This project is under active development. New features, AI capabilities, and frontend components will be added continuously.