# 🛡️ AI Surveillance Platform

> **Helping security teams turn continuous camera activity into actionable security events instead of relying entirely on manual monitoring.**

Monitoring multiple surveillance feeds becomes increasingly difficult as the number of cameras and monitored areas grows. The challenge is not simply capturing video — it is identifying **what happened, who was involved, when it happened, and whether the event requires attention**.

The **AI Surveillance Platform** is being built to address this problem by combining computer vision, event tracking, centralized APIs, and analytics into a modular surveillance backend.

Instead of treating surveillance as a collection of camera feeds, the platform is designed around a pipeline that turns camera activity into structured information:

```text
Camera Activity
      │
      ▼
Detection
      │
      ▼
Recognition
      │
      ▼
Event
      │
      ▼
Alert / Analytics
```

The project is being developed incrementally, starting with the backend and data infrastructure and expanding toward AI-powered detection, recognition, event monitoring, analytics, and alerting.

## 🚧 Project Status: Active Development

## 📖 Why This Project?

Traditional surveillance systems are effective at providing access to video feeds, but continuous human monitoring does not scale well.

A surveillance platform becomes more useful when it can answer questions such as:

- What happened?
- When did it happen?
- Which camera captured it?
- Was a person detected?
- Was the person recognized?
- Was the event expected or suspicious?
- Should an alert be generated?
- Can the event be analyzed later?

The goal of this project is therefore to build a centralized surveillance backend that can support these workflows while keeping the individual components modular.

The platform is designed so that computer-vision models can be integrated into the system without tightly coupling AI inference to the rest of the application.

## 🎯 What the Platform Is Designed to Provide

The platform aims to provide:

- Real-time person detection
- Face recognition
- Camera management
- Event logging
- Security alerts
- Analytics
- REST APIs
- Dockerized deployment

The architecture is intentionally modular so additional AI models, processing services, and deployment infrastructure can be introduced without redesigning the entire system.

## ✨ Features & Development Status

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

## 🏗️ Project Architecture

The system is organized around a modular backend where detection, recognition, analytics, and storage can evolve independently.

```text
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

The current implementation focuses on establishing the backend and data foundation required for these services.

## 🧠 AI Processing Pipeline

The intended surveillance workflow is:

```text
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

This separates the computer-vision pipeline from the application layer.

The detection and recognition services can therefore be developed independently while the backend handles persistence, APIs, events, and future analytics.

> **Note:** Detection, recognition, event logging, analytics, and alerting components are currently being developed and are not all fully implemented yet.

## 📂 Project Structure

```text
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

The service structure is designed to keep major surveillance capabilities isolated:

```text
services/
├── alerts/
├── analytics/
├── camera/
├── detection/
├── recognition/
└── storage/
```

This makes it possible to extend or replace individual components as the platform evolves.

## ⚙️ Tech Stack

**Backend**
- FastAPI
- Python
- SQLAlchemy
- Pydantic
- Uvicorn

**Database**
- PostgreSQL

**AI & Computer Vision**
- OpenCV
- InsightFace (Planned)
- YOLO (Planned)

**DevOps**
- Docker
- Docker Compose

**Frontend**
- React (Planned)
- Axios (Planned)
- Tailwind CSS (Planned)

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sachint19004/ai-surveillance-platform.git
cd ai-surveillance-platform
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux / macOS:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file.

Example:
```env
APP_NAME=AI Surveillance Platform
APP_VERSION=1.0.0

DATABASE_URL=postgresql://postgres:password@localhost:5432/ai_surveillance

SECRET_KEY=your-secret-key

DEBUG=True
```

### 5. Start PostgreSQL

The project uses Docker for the database environment.
```bash
docker compose up -d
```

### 6. Run FastAPI
```bash
uvicorn app.main:app --reload
```

### 7. Open Swagger

Once the backend is running:

http://127.0.0.1:8000/docs


Swagger/OpenAPI provides an interactive interface for exploring the available API endpoints.

## 📡 API

The backend is organized around modular API capabilities.

Current API modules include:

- Authentication (Planned)
- Users
- Camera
- Detection
- Recognition
- Events
- Analytics

Swagger UI is available at:

/docs

The API layer is intended to provide a consistent interface between the frontend, surveillance services, and database.

## 🗄️ Database

The current database structure includes support for:

- Users
- Authorized Faces
- Cameras
- Events
- Alerts
- Recognition Logs

Conceptually:

```text
Users
  │
  ├── Authorized Faces
  │
  ├── Cameras
  │
  ├── Events
  │
  ├── Alerts
  │
  └── Recognition Logs
```

More tables will be added as the platform evolves.

The database is designed to store structured surveillance information rather than treating the system purely as a video-processing application.

## 🔌 Backend Responsibilities

The backend acts as the central coordination layer between the different parts of the platform.

```text
                    ┌───────────────────┐
                    │   Camera / Input  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Detection Service │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │Recognition Service│
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Event Processing │
                    └─────────┬─────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        ┌───────────────┐           ┌───────────────┐
        │ Alert Service │           │   Analytics   │
        └───────────────┘           └───────────────┘
                │                           │
                └─────────────┬─────────────┘
                              ▼
                       PostgreSQL
```

This separation allows AI inference and business/application logic to remain independently maintainable.

## 🛣️ Roadmap

**Phase 1 — Platform Foundation**
- [x] Backend Setup
- [x] PostgreSQL
- [x] Docker
- [x] Project Architecture

**Phase 2 — Computer Vision**
- [ ] Detection Service
- [ ] Recognition Service
- [ ] Camera APIs

**Phase 3 — Application Layer**
- [ ] React Dashboard
- [ ] Authentication
- [ ] Analytics
- [ ] Event Processing
- [ ] Alert System

**Phase 4 — Production Infrastructure**
- [ ] Deployment
- [ ] CI/CD
- [ ] Kubernetes
- [ ] Cloud Hosting
- [ ] Monitoring

## 🔭 Future Direction

The long-term goal is to evolve the project from a backend foundation into a complete surveillance platform.

Potential capabilities include:

```text
Multiple Cameras
       │
       ▼
Real-Time Video
       │
       ▼
AI Detection
       │
       ▼
Face Recognition
       │
       ▼
Event Intelligence
       │
       ├──────────────► Alerts
       │
       ├──────────────► Analytics
       │
       └──────────────► Historical Events
                              │
                              ▼
                         Dashboard
```

Additional infrastructure such as Redis, Celery, Kubernetes, and cloud deployment can eventually support higher workloads and distributed processing.

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

## 📜 License

This project is currently licensed under the MIT License.

## 👨‍💻 Author

**Sachin T**

- GitHub: [https://github.com/sachint19004](https://github.com/sachint19004)
- LinkedIn: [https://www.linkedin.com/in/sachin-taspire19/](https://www.linkedin.com/in/sachin-taspire19/)

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ Star on GitHub.

It helps support the project and motivates further development.

---

🚀 This project is under active development. New AI capabilities, surveillance services, and frontend components will be added incrementally.
