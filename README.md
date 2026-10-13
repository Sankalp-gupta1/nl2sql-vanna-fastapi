# NL2SQL — Vanna + FastAPI

A natural-language-to-SQL project built around a clinic database.

## Live demo

**https://nl2sql-vanna-fastapi.vercel.app/**

The repository contains two modes:

1. the original **Vanna + Gemini + FastAPI** implementation,
2. a public **keyless browser demo**.

## Live keyless demo

The deployed version lets a reviewer type common clinic questions and see the full flow:

```text
question
   ↓
generated SQL
   ↓
SQLite execution
   ↓
result table
```

It uses SQL.js / SQLite in the browser and a deterministic question mapper.

No API key or database password is required.

## Example questions

- How many patients are there?
- Show patients from Kanpur
- List cardiology doctors
- Show pending invoices
- Total invoice amount by status
- Count appointments by status
- Top doctors by appointment count
- Average treatment cost

The generated SQL is visible and editable.

The web demo only executes read-only `SELECT` queries.

## Original AI backend

The original Python project uses:

- FastAPI
- Vanna AI
- Gemini
- SQLite
- `clinic.db`

That version requires:

```text
GOOGLE_API_KEY
```

The AI-backed code is preserved in the repository.

## Why there are two modes

A public portfolio should not expose a private Gemini key.

The keyless browser version makes the project usable by reviewers without pretending that an LLM is available when no key is configured.

## Run the web demo locally

```bash
cd web
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

## Run the original Vanna backend

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Gemini

Create a local `.env` file:

```text
GOOGLE_API_KEY=your_key_here
```

### 3. Prepare the database

Use the included database/setup scripts if needed.

### 4. Start FastAPI

Run the project's FastAPI entry point.

## Tech stack

### AI mode
- Python
- FastAPI
- Vanna AI
- Gemini
- SQLite

### Hosted mode
- HTML
- CSS
- JavaScript
- SQL.js
- SQLite
- Vercel

## Author

**Sankalp Gupta**

- GitHub: https://github.com/Sankalp-gupta1
- LinkedIn: https://www.linkedin.com/in/sankalp-gupta-rishi-8617302b0/
