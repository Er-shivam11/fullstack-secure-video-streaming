Here’s your final `README.md`, customized based on your project structure, removed folders (`.dbdata`, `node_modules`,`*.json`), and Docker + DRF + React + Kafka stack:

---

```markdown
# 🎥 Encrypted Video Upload & Playback System

A full-stack video upload and playback system using **Django REST Framework**, **React**, **Kafka**, and **Docker**. Uploaded videos are encrypted before saving and can be decrypted during download using secure backend APIs.

---

## 🎥 Demo

[▶️ Click to watch the demo video](./demo.mp4)


## 🧱 Stack

- [x] Python 3.8
- [x] Django + Django REST Framework (DRF)
- [x] React
- [x] aiokafka
- [x] kafka-python
- [x] Docker + Docker Compose
- [x] MySQL + phpMyAdmin
- [x] Kafdrop (Kafka UI)

---

## 📁 Project Structure
├──video/  frontend
|
├── video_uploader/ backend
|
├── docker-compose.yml               ← Docker Compose configuration file(zookeeper,kafka,kafdrop1)
└── README.md


> 🧹 **Excluded from version control**:
> - `.dbdata/` (MySQL volume)
> - `node_modules/` & `*json` (React dependencies)

---

## 🚀 How to Use

### Step 1: Prerequisites

- Make sure you have Docker and Docker Compose installed:
  - [Docker Install Guide](https://docs.docker.com/get-docker/)

---

### Step 2: Start All Services

```bash
docker-compose up --build
```

Docker Compose will set up and start the following containers:

| Container         | Description                      |
|------------------|----------------------------------|
| `react_frontend` | React app for video UI           |
| `video_uploader` | Django + DRF API backend         |
| `kafka`          | Kafka broker                     |
| `zookeeper`      | Kafka zookeeper                  |
| `kafdrop`        | Kafka monitoring UI              |
| `db`             | MySQL database                   |
| `phpmyadmin`     | MySQL Admin UI                   |

---

## 🌐 Port Overview

| Service        | Port     | URL                          |
|----------------|----------|------------------------------|
| Frontend       | 3000     | http://localhost:3000        |
| Backend API    | 8000     | http://localhost:8000        |
| Kafka UI       | 19000    | http://localhost:19000       |
| phpMyAdmin     | 9092     | http://localhost:9092        |


## 🔌 URL Endpoints

### 🔧 Backend API (Django REST)

| Action           | URL                                | Method |
|------------------|-------------------------------------|--------|
| Upload Video     | `http://localhost:8000/api/upload/` | POST   |
| Get Encrypted    | `http://localhost:8000/api/upload/?id=<video_id>` | GET |

### 🎬 Frontend UI (React)

- `http://localhost:3000`  
- `http://localhost:3000/upload` 
- `http://localhost:3000/stream/1` 
  Upload and play encrypted videos from the browser.

### 📊 Kafka Dashboard (Kafdrop)

- `http://localhost:19000`  
  View Kafka topics and messages.

### 🗄️ phpMyAdmin (MySQL DB)

- `http://localhost:9092`  
  Access database with:
  - Server: `db`
  - Username: `root`
  - Password: `root`

---

## 📌 Notes

- Ensure video files are MP4 format for compatibility.
- Videos are encrypted using AES before storage and decrypted on request.
- Kafka producer logs upload metadata; 

---

## 📬 Contact

For any issues, feel free to raise an issue or reach out.

---
```

