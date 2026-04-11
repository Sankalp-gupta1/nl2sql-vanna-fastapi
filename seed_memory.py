from vanna_setup import vn

training_data = [

("Show all patients",
 "SELECT * FROM patients;"),

("Show all doctors",
 "SELECT * FROM doctors;"),

("Show all appointments",
 "SELECT * FROM appointments;"),

("List patients from Delhi",
 "SELECT * FROM patients WHERE city='Delhi';"),

("Show completed appointments",
 "SELECT * FROM appointments WHERE status='Completed';"),

("Show cancelled appointments",
 "SELECT * FROM appointments WHERE status='Cancelled';"),

("Count total patients",
 "SELECT COUNT(*) FROM patients;"),

("Count total doctors",
 "SELECT COUNT(*) FROM doctors;"),

("Show treatments costing more than 1000",
 "SELECT * FROM treatments WHERE cost > 1000;"),

("Show unpaid invoices",
 "SELECT * FROM invoices WHERE status='Pending';"),

("Show overdue invoices",
 "SELECT * FROM invoices WHERE status='Overdue';"),

("List all male patients",
 "SELECT * FROM patients WHERE gender='M';"),

("List all female patients",
 "SELECT * FROM patients WHERE gender='F';"),

("Show today's appointments",
 "SELECT * FROM appointments WHERE DATE(appointment_date)=DATE('now');"),

("Show total invoice amount",
 "SELECT SUM(total_amount) FROM invoices;")

]

for question, sql in training_data:
    vn.train(question=question, sql=sql)

print("✅ Memory seeded successfully!")