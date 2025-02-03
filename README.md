# Patient Tracking and Management System

## Overview
This project involves the development of a **web application** designed to assist patients in managing their medical processes. The **Patient Tracking and Management System** allows patients to:

- Register and manage their profiles.
- Schedule and cancel appointments with doctors.
- Securely store and access medical reports.
- Handle general health operations through a user-friendly interface.

Built with **Python** and **MySQL**, the project employs principles of **object-oriented programming**, database normalization, and robust security measures. The platform features dynamic components, an intuitive UI, and seamless interactions to ensure an optimal user experience.

## Table of Contents
- [Overview](#overview)
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Database Design](#database-design)
- [Object-Oriented Programming](#object-oriented-programming)
- [Security Measures](#security-measures)
- [User Interface](#user-interface)
- [Backend Implementation](#backend-implementation)
- [Pseudocode](#pseudocode)
- [Results](#results)
- [Screenshots](#screenshots)
- [References](#references)

## Introduction
In today's digital age, healthcare services need to keep up with the pace of technological advancements. Traditional methods of managing patient records, appointments, and medical reports are often time-consuming and prone to errors. Digitalizing these processes improves efficiency, reliability, and accessibility, ultimately enhancing the quality of healthcare services.

The **Patient Tracking and Management System** addresses this need by offering a web-based solution for patients and healthcare professionals. It ensures streamlined processes, secure data handling, and a highly interactive interface. This project emphasizes:

- Simplifying patient registration and management.
- Enabling efficient appointment scheduling and cancellation.
- Safeguarding medical records with secure storage and access.
- Providing dynamic and intuitive UI/UX designs.

## Technologies Used
- **Programming Language:** Python (Flask Framework)
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript (AJAX)
- **Libraries/Tools:** Bootstrap, JSON, Flask-WTF
- **Security Protocols:** HTTPS, Password Hashing (SHA-256)

## Features
1. **Patient Management:**
   - Add, update, and delete patient records.
2. **Doctor Management:**
   - Register, update, and remove doctors.
   - Restrict deletion for doctors with active appointments.
3. **Appointment Management:**
   - Schedule, update, or cancel appointments.
4. **Medical Reports:**
   - Upload, view, and manage patient medical reports securely.
5. **Dynamic Interface:**
   - Interactive dashboards for patients and doctors.
   - Notifications for new updates or reports.
6. **Security:**
   - Secure HTTPS connections and encrypted sensitive data.

## Database Design
The relational database design ensures data consistency and integrity with primary and foreign key relationships. Key tables include:

- **Patients:** Stores patient details.
- **Doctors:** Stores doctor information.
- **Appointments:** Tracks patient-doctor interactions.
- **Medical Reports:** Stores medical records with file URLs and content.
- **Admins:** Handles administrative user management.

## Object-Oriented Programming
The system uses OOP principles for modular design:

### Key Classes and Methods:
- **Patient Class**
  - Methods: `add_patient()`, `update_patient()`, `delete_patient()`
- **Doctor Class**
  - Methods: `add_doctor()`, `update_doctor()`, `delete_doctor()`
- **Appointment Class**
  - Methods: `schedule_appointment()`, `cancel_appointment()`, `update_appointment()`
- **MedicalReport Class**
  - Methods: `add_report()`, `delete_report()`, `update_report()`

## Security Measures
1. **HTTPS Protocol:** Ensures secure data transmission.
2. **Password Hashing:** Uses SHA-256 for storing sensitive credentials.
3. **Role-Based Access Control:** Restricts access to sensitive actions based on user roles.
4. **Input Validation:** Prevents SQL injection and XSS attacks.

## User Interface
The UI offers dynamic and interactive features for enhanced user experience:

1. **Dashboard:** Displays personalized details for patients and doctors.
2. **Dynamic Components:**
   - AJAX-based updates for seamless interactions.
   - Notifications for important updates or alerts.
3. **Search & Filter:**
   - Query appointments, medical records, and profiles in real-time.

## Backend Implementation
1. **Flask Framework:**
   - Provides REST APIs for all major functions (CRUD operations).
2. **Database Integration:**
   - Uses MySQL for reliable and consistent data storage.
3. **Trigger Functions:**
   - Automates cascading updates or deletions across related tables.

## Pseudocode
```python
# Flask Server Initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@host/db_name'

@app.route('/patients', methods=['GET'])
def get_patients():
    # Fetch all patients from the database
    return jsonify(fetch_all_patients())

@app.route('/appointments', methods=['POST'])
def create_appointment():
    # Parse appointment details from the request
    # Validate and insert into the database
    return jsonify({"message": "Appointment created successfully"})
```

## Results
### Observations:
1. **Successful Patient Management:**
   - Patients can be added, updated, or removed seamlessly.
2. **Robust Appointment Handling:**
   - Real-time booking and cancellation with automatic database updates.
3. **Secure Medical Records:**
   - Encrypted storage and role-based access ensure confidentiality.
4. **Interactive Dashboard:**
   - Simplified navigation for patients and doctors.

### Achievements:
- Fully operational web-based healthcare management system.
- Reliable database design ensuring consistency and integrity.
- Intuitive and secure user interface for all stakeholders.

## Screenshots
### Web Application Interface
![Web Application Screenshot](images1/FireShot Capture 001 - Hastane Yönetim Sistemi - [127.0.0.1].png)

## References
- Elmasri, R., & Navathe, S. B. (2010). *Fundamentals of Database Systems*. Addison-Wesley.
- Sommerville, I. (2011). *Software Engineering*. Addison-Wesley.
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
- Flask Documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
