# ⚡ NeuroFeed — AI-Powered Personalized Learning Platform

![NeuroFeed Banner](https://img.shields.io/badge/NeuroFeed-AI%20Study%20Planner-6366f1?style=for-the-badge&logo=lightning&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3%2070B-f97316?style=for-the-badge)

> Generate personalized, day-by-day study plans powered by Llama 3.3 70B AI — tailored to your topic, goal, and timeline.

---

## 🚀 Live Demo

Type your topic → Set your goal → Get a full AI-generated study plan in seconds.

![NeuroFeed UI](https://img.shields.io/badge/Status-Live%20Locally-22c55e?style=flat-square)

---

## ✨ Features

- 🤖 **AI Study Plan Generation** — Powered by Llama 3.3 70B via Groq API
- 📅 **Custom Duration** — Choose anywhere from 7 to 90 days
- 💾 **Plan Storage** — Every generated plan saved to PostgreSQL
- 🔐 **User Auth** — Register and login system with hashed passwords
- 🌐 **REST API** — Clean Django REST Framework endpoints
- ⚡ **Fast UI** — React frontend with real-time loading states
- 🎨 **Dark Theme** — Clean, modern dark UI with gradient accents

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Django 6.0, Django REST Framework |
| **Frontend** | React 18, Axios |
| **Database** | PostgreSQL 17 |
| **AI** | Groq API — Llama 3.3 70B Versatile |
| **Auth** | SHA-256 password hashing |
| **Styling** | Custom CSS with dark theme |

---

## 📁 Project Structure

```
NeuroFeed/
├── neurofeed_backend/        # Django project root
│   ├── settings.py           # Project configuration
│   └── urls.py               # Root URL routing
├── users/                    # User auth app
│   ├── models.py             # CustomUser model
│   ├── views.py              # Register + Login views
│   └── urls.py               # Auth endpoints
├── courses/                  # Courses & progress app
│   └── models.py             # Topic + UserProgress models
├── studyplans/               # AI study plan app
│   ├── models.py             # StudyPlan model
│   ├── views.py              # AI generation logic
│   └── urls.py               # Study plan endpoints
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── App.js            # Main UI component
│   │   └── App.css           # Dark theme styles
│   └── package.json
└── .env                      # Environment variables (not committed)
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/users/register/` | Register new user |
| `POST` | `/api/users/login/` | Login user |
| `POST` | `/api/studyplans/generate/` | Generate AI study plan |
| `GET` | `/api/studyplans/user/<id>/` | Get all plans for a user |

### Example Request — Generate Study Plan

```bash
curl -X POST http://127.0.0.1:8000/api/studyplans/generate/ \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Python Django",
    "goal": "Build REST APIs and get placed",
    "duration_days": 30,
    "user_id": 1
  }'
```

### Example Response

```json
{
  "id": 1,
  "topic": "Python Django",
  "goal": "Build REST APIs and get placed",
  "duration_days": 30,
  "plan": "**30-Day Study Plan: Python Django**\n\n### Day 1: Introduction...",
  "created_at": "2026-06-29T02:10:17Z"
}
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 17
- Groq API Key (free at console.groq.com)

### 1. Clone the repo

```bash
git clone https://github.com/ennyatha/NeuroFeed.git
cd NeuroFeed
```

### 2. Backend Setup

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install django djangorestframework psycopg2-binary python-dotenv groq django-cors-headers

# Create .env file
cp .env.example .env
# Fill in your values in .env
```

### 3. Configure .env

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=neurofeed_db
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
GROQ_API_KEY=your-groq-api-key
```

### 4. Database Setup

```bash
# Create database in PostgreSQL first, then:
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Backend

```bash
python manage.py runserver
# API live at http://127.0.0.1:8000
```

### 6. Frontend Setup

```bash
cd frontend
npm install
npm start
# UI live at http://localhost:3000
```

---

## 🗄️ Database Schema

```
users
├── id (PK)
├── username (unique)
├── email (unique)
├── password (SHA-256 hashed)
├── full_name
└── created_at

studyplans_studyplan
├── id (PK)
├── user_id (FK)
├── topic
├── goal
├── duration_days
├── plan_content (AI generated text)
└── created_at

courses_topic
├── id (PK)
├── name
├── description
└── created_at

courses_userprogress
├── id (PK)
├── user_id
├── topic_id (FK)
├── completed
├── score
└── updated_at
```

---

## 🔮 Roadmap

- [ ] JWT Authentication
- [ ] User dashboard with plan history
- [ ] Progress tracking per day
- [ ] Email reminders via Celery
- [ ] Docker containerization
- [ ] AWS deployment (EC2 + RDS)
- [ ] Mobile responsive UI improvements

---

## 👩‍💻 Author

**Chavali Ennyatha Yadav**
B.Tech CSE (Networking) — SRMIST Chennai, 2027

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/ennyatha-chavali-55b727287)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/ennyatha)

---

## 📄 License

MIT License — feel free to use, modify and build on this project.
