import os
from dotenv import load_dotenv

from vanna.sqlite import SQLiteVanna
from vanna.llm import Gemini

# Load API key
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY missing in .env file")

# Setup LLM
vn = SQLiteVanna(
    llm=Gemini(
        api_key=api_key,
        model="gemini-1.5-flash"
    ),
    db_path="clinic.db"
)

# Train Schema
def train_schema():

    vn.train("""
    patients(
        id,
        first_name,
        last_name,
        email,
        phone,
        date_of_birth,
        gender,
        city,
        registered_date
    )

    doctors(
        id,
        name,
        specialization,
        department,
        phone
    )

    appointments(
        id,
        patient_id,
        doctor_id,
        appointment_date,
        status,
        notes
    )

    treatments(
        id,
        appointment_id,
        treatment_name,
        cost,
        duration_minutes
    )

    invoices(
        id,
        patient_id,
        invoice_date,
        total_amount,
        paid_amount,
        status
    )
    """)

    print("✅ Schema trained successfully!")

if __name__ == "__main__":
    train_schema()