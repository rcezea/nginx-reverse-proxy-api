# 🚀 Nginx Reverse Proxy API

This is a simple API built with FastAPI to demonstrate a lightweight backend service that can be used behind an Nginx reverse proxy.

---
## 🌐 Live Deployment

Base URL:
http://devops.rclancing.dev/
---
## 📦 Repository

```
git@github.com:rcezea/nginx-reverse-proxy-api.git
```

---

## ⚙️ Features

* ✅ Simple REST API
* ✅ Health check endpoint
* ✅ CORS enabled (allowing all origins)
* ✅ JSON responses with explicit status codes

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/rcezea/nginx-reverse-proxy-api.git
cd nginx-reverse-proxy-api
```

### 2. Install dependencies

Make sure you have Python installed, then:

```bash
pip install requirements.txt
```

---

## ▶️ Running the API

Start the development server:

```bash
fastapi dev
```

By default, the API runs on:

```
http://localhost:8000
```

---

## 📡 API Endpoints

### `GET /`

**Description:** Root endpoint to verify the API is running

**Response:**

```json
{
  "message": "API is running"
}
```

---

### `GET /health`

**Description:** Health check endpoint

**Response:**

```json
{
  "message": "healthy"
}
```

---

### `GET /me`

**Description:** Returns profile information

**Response:**

```json
{
  "name": "Richard Ezea",
  "email": "rclancing@gmail.com",
  "github": "https://github.com/rcezea"
}
```

---

## 🌐 CORS Configuration

CORS is enabled using middleware:

* Allows all origins (`*`)
* Allows GET HTTP method

---

## 📁 Project Structure

```
.
├── main.py   # FastAPI application
└── README.md
```

---

## 🧪 Testing

You can test the API using:

* Browser → `http://localhost:8000`
* cURL:

  ```bash
  curl http://localhost:8000/health
  ```
* Postman or any API client

---

## 📝 Notes

* Responses are returned using `JSONResponse`
* Status codes are explicitly defined
* Designed to be used behind an Nginx reverse proxy setup

---

## 👤 Author

**Richard Ezea**

* GitHub: https://github.com/rcezea
* Email: [rclancing@gmail.com](mailto:rclancing@gmail.com)

---

## 📄 License

This project is open-source and available under the MIT License.
