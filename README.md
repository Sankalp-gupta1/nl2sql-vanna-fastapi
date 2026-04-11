 # 🧠 Natural Language to SQL (NL2SQL) System using Vanna AI & FastAPI

## 📌 Project Title
**NL2SQL System using Vanna AI and FastAPI with SQLite Database**

---

# 📖 Abstract

This project presents an end-to-end implementation of a **Natural Language to SQL (NL2SQL)** system designed to convert human-readable natural language queries into executable SQL statements.

The system leverages **Vanna AI** for semantic SQL generation and **FastAPI** for high-performance API deployment. It enables users to interact with relational databases without prior SQL knowledge.

The system architecture includes:

- Database initialization
- Schema training
- Memory-based SQL learning
- API-based query execution
- Natural language interface

This project demonstrates applied skills in:

- Large Language Models (LLMs)
- Backend API Development
- Database Engineering
- Natural Language Processing
- AI-driven Query Systems

---

# 🎯 Project Objectives

The primary goals of this project are:

✔ Build a working NL2SQL pipeline  
✔ Enable database querying using natural language  
✔ Integrate Vanna AI with SQLite  
✔ Deploy a scalable REST API  
✔ Create reusable schema memory  
✔ Support dynamic SQL generation  
✔ Provide production-style documentation  

---

# 🏗 System Architecture


User Query (Natural Language)

↓

FastAPI

↓

Vanna AI

↓

SQL Generation

↓

SQLite DB

↓

Query Result

↓

API Response


---

# 🧩 Core Components

This system consists of multiple modular components:

---

## 1️⃣ Database Initialization Module

File:


setup_database.py


Responsibilities:

- Creates SQLite database
- Defines tables
- Inserts realistic dummy data
- Simulates healthcare workflow dataset

Tables created:

- Doctors
- Patients
- Appointments
- Treatments
- Specializations

---

## 2️⃣ Vanna Configuration Module

File:


vanna_setup.py


Responsibilities:

- Initializes Vanna AI
- Connects to SQLite database
- Loads schema metadata
- Enables SQL generation
- Configures API key environment

---

## 3️⃣ Memory Training Module

File:


seed_memory.py


Responsibilities:

- Trains Vanna model
- Adds known SQL examples
- Improves query accuracy
- Enhances semantic understanding

Example:


Question:
Show all doctors

SQL:
SELECT * FROM doctors;


---

## 4️⃣ API Server Module

File:


main.py


Responsibilities:

- Creates REST API
- Accepts natural language queries
- Converts query → SQL
- Executes SQL
- Returns structured results

Framework Used:


FastAPI


---

# 📂 Project Directory Structure


nl2sql-vanna-fastapi/
│
├── main.py
├── setup_database.py
├── seed_memory.py
├── vanna_setup.py
├── clinic.db
├── requirements.txt
├── .gitignore
├── README.md
│
└── pycache/


---

# ⚙️ Installation Guide (Step-by-Step)

Follow these steps to run the system locally.

---

## Step 1 — Clone Repository


git clone https://github.com/Sankalp-gupta1/nl2sql-vanna-fastapi.git


---

## Step 2 — Move to Project Folder


cd nl2sql-vanna-fastapi


---

## Step 3 — Install Dependencies


pip install -r requirements.txt


---

## Step 4 — Setup Environment Variables

Create:


.env


Add:


GOOGLE_API_KEY=your_api_key_here


⚠ Important:

Do NOT upload `.env` to GitHub.

---

## Step 5 — Create Database

Run:


python setup_database.py


Output:


Database created successfully
Dummy data inserted successfully


---

## Step 6 — Train Model Memory

Run:


python seed_memory.py


Purpose:

- Train SQL examples
- Improve accuracy

---

## Step 7 — Start API Server

Run:


uvicorn main:app --reload


Server will start at:


http://127.0.0.1:8000


---

# 🌐 API Documentation

Open in browser:


http://127.0.0.1:8000/docs


This opens:

**Swagger UI Interface**

You can test queries directly.

---

# 🧪 Example Queries

Try these:


Show all doctors

List all patients

Show today's appointments

Count total appointments

List doctors by specialization

Show patient appointments


---

# 🔍 How the System Works (Detailed Flow)

1. User sends natural language query
2. FastAPI receives request
3. Vanna AI converts query → SQL
4. SQL executes on SQLite database
5. Result returned as JSON
6. User receives readable output

---

# 📊 Database Design Overview

Database used:


SQLite


Schema includes:

## Doctors Table


doctor_id
name
specialization
experience


## Patients Table


patient_id
name
age
gender


## Appointments Table


appointment_id
patient_id
doctor_id
date
status


---

# 🧠 Machine Learning Concept Used

This project uses:


Natural Language Processing
Semantic SQL Generation
Memory-based Query Learning
LLM-driven SQL synthesis


---

# 🚀 How to Use This System in Your Own Projects

You can integrate this system into:

✔ Hospital Management Systems  
✔ CRM Analytics Systems  
✔ Business Intelligence Tools  
✔ Customer Query Systems  
✔ Data Dashboard Applications  

Steps:

1. Replace database schema
2. Train new SQL examples
3. Deploy FastAPI
4. Connect frontend UI

---

# 🧪 Testing Guide

Test via:


Swagger UI


Or:


Postman


Send:


POST /query


Body:


{
"question": "Show all doctors"
}


---

# 🔐 Security Practices

✔ `.env` excluded  
✔ API keys hidden  
✔ Database isolated  
✔ Git-safe configuration  

---

# 📈 Performance Considerations

Optimizations:

✔ Indexed tables  
✔ Schema-aware SQL  
✔ Cached query memory  
✔ FastAPI async support  

---

# 🧰 Technologies Used


Python
FastAPI
Vanna AI
SQLite
Pandas
Faker
Uvicorn


---

# 🧑‍💻 Developer Skills Demonstrated

✔ Backend Development  
✔ Database Engineering  
✔ LLM Integration  
✔ REST API Design  
✔ AI System Deployment  
✔ Software Architecture  

---

# 🧪 Future Improvements

Possible upgrades:

✔ Add Streamlit UI  
✔ Add PostgreSQL support  
✔ Add authentication  
✔ Add query caching  
✔ Deploy on cloud  

---

# 📦 Deployment Possibilities

This project can be deployed on:

✔ AWS  
✔ Azure  
✔ GCP  
✔ Docker  
✔ Render  
✔ Railway  

---

# 📚 Learning Outcomes

From this project:

✔ Learned NL2SQL pipeline  
✔ Learned API development  
✔ Learned schema training  
✔ Learned LLM-based SQL generation  

---

# 📌 Author

**Sankalp Gupta**  
AI/ML Developer Intern Candidate  

GitHub:


https://github.com/Sankalp-gupta1


---

# 📄 License

This project is created for:


AI/ML Developer Internship Assignment
