import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# STEP 1 — Create Tables

def create_database():
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    # Patients Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        date_of_birth DATE,
        gender TEXT,
        city TEXT,
        registered_date DATE
    )
    """)

    # Doctors Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT,
        department TEXT,
        phone TEXT
    )
    """)

    # Appointments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date DATETIME,
        status TEXT,
        notes TEXT
    )
    """)

    # Treatments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS treatments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id INTEGER,
        treatment_name TEXT,
        cost REAL,
        duration_minutes INTEGER
    )
    """)

    # Invoices Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        invoice_date DATE,
        total_amount REAL,
        paid_amount REAL,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

    print("Database and tables created successfully!")

# STEP 2 — Insert Dummy Data

def insert_dummy_data():

    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    specializations = [
        "Dermatology",
        "Cardiology",
        "Orthopedics",
        "General",
        "Pediatrics"
    ]

    cities = [
        "Delhi",
        "Mumbai",
        "Pune",
        "Lucknow",
        "Kanpur",
        "Bangalore",
        "Chennai",
        "Hyderabad"
    ]

    # Doctors

    doctor_ids = []

    for _ in range(15):

        cursor.execute("""
        INSERT INTO doctors (name, specialization, department, phone)
        VALUES (?, ?, ?, ?)
        """, (
            fake.name(),
            random.choice(specializations),
            random.choice(specializations),
            fake.phone_number()
        ))

        doctor_ids.append(cursor.lastrowid)

    # Patients

    patient_ids = []

    for _ in range(200):

        cursor.execute("""
        INSERT INTO patients
        (first_name,last_name,email,phone,
        date_of_birth,gender,city,registered_date)
        VALUES (?,?,?,?,?,?,?,?)
        """, (

            fake.first_name(),
            fake.last_name(),

            fake.email() if random.random() > 0.2 else None,

            fake.phone_number() if random.random() > 0.2 else None,

            fake.date_of_birth(minimum_age=18, maximum_age=80),

            random.choice(["M", "F"]),

            random.choice(cities),

            fake.date_between(start_date="-12M", end_date="today")

        ))

        patient_ids.append(cursor.lastrowid)

    # Appointments

    appointment_ids = []

    for _ in range(500):

        appointment_date = datetime.now() - timedelta(
            days=random.randint(0, 365)
        )

        cursor.execute("""
        INSERT INTO appointments
        (patient_id,doctor_id,
        appointment_date,status,notes)
        VALUES (?,?,?,?,?)
        """, (

            random.choice(patient_ids),

            random.choice(doctor_ids),

            appointment_date,

            random.choice([
                "Scheduled",
                "Completed",
                "Cancelled",
                "No-Show"
            ]),

            fake.sentence() if random.random() > 0.3 else None

        ))

        appointment_ids.append(cursor.lastrowid)

    # Treatments

    for _ in range(350):

        cursor.execute("""
        INSERT INTO treatments
        (appointment_id,treatment_name,
        cost,duration_minutes)
        VALUES (?,?,?,?)
        """, (

            random.choice(appointment_ids),

            random.choice([
                "Checkup",
                "X-Ray",
                "Surgery",
                "Therapy",
                "Consultation"
            ]),

            random.randint(50, 5000),

            random.randint(10, 120)

        ))

    # Invoices

    for _ in range(300):

        total = random.randint(100, 5000)

        cursor.execute("""
        INSERT INTO invoices
        (patient_id,invoice_date,
        total_amount,paid_amount,status)
        VALUES (?,?,?,?,?)
        """, (

            random.choice(patient_ids),

            fake.date_between(start_date="-12M", end_date="today"),

            total,

            random.randint(0, total),

            random.choice([
                "Paid",
                "Pending",
                "Overdue"
            ])

        ))

    conn.commit()
    conn.close()

    print("Dummy data inserted successfully!")

# MAIN

if __name__ == "__main__":

    create_database()

    insert_dummy_data()