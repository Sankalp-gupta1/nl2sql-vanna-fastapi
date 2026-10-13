# NL2SQL — Vanna + FastAPI

## Live app

**https://nl2sql-vanna-fastapi.vercel.app/**

The repository now also includes a **keyless public demo** in `web/`. It creates an in-browser SQLite database, converts common analytics questions into deterministic SQL, executes the SQL, and renders the result table.

This does not pretend to replace Vanna AI. It is a hosted fallback that lets reviewers test the NL → SQL → execution workflow without supplying an LLM key or database credential. The original Vanna/FastAPI code remains the LLM-backed architecture reference.

Example hosted questions include:

- total revenue
- top customers by revenue
- completed order count
- latest orders
- average order value

### Run the web demo locally

```bash
cd web
python -m http.server 8000
```

---

A natural-language-to-SQL project built around a clinic database.

## Live demo

**https://nl2sql-clinic-sankalp.vercel.app/**

## Two modes

### Original LLM backend

The original Python project uses:

- FastAPI
- Vanna AI
- Gemini
- SQLite
- `clinic.db`

It needs a `GOOGLE_API_KEY`.

### Deployed offline mode

The new `web/` version works without any secret.

It uses:

- SQL.js / SQLite in the browser
- a deterministic natural-language mapper for common clinic questions
- editable generated SQL
- a read-only execution rule that accepts only `SELECT` queries
- a seeded clinic dataset

This lets a reviewer see the full flow:

```text
question → generated SQL → SQLite execution → table result
```

without needing my private Gemini key.

## Example questions

- How many patients are there?
- Show patients from Kanpur
- List cardiology doctors
- Show pending invoices
- Total invoice amount by status
- Count appointments by status
- Top doctors by appointment count
- Average treatment cost

## Run the live web version locally

```bash
cd web
python -m http.server 8000
```

Open `http://localhost:8000`.

## Run the original Vanna backend

1. Install the Python requirements.
2. Create a `.env` file.
3. Add `GOOGLE_API_KEY`.
4. Run the database setup if needed.
5. Start FastAPI.

The original backend files are preserved and are not replaced by the offline demo.

## Why the fallback exists

A public portfolio should not expose a private LLM key. The deterministic mode makes the project usable without pretending that Gemini is available when no key is configured.

## Author

Sankalp Gupta  
GitHub: https://github.com/Sankalp-gupta1
