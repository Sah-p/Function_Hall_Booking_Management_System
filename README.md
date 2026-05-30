#  Function Hall Booking Management System

A full-stack web application for browsing, booking, and managing function halls. Developed as a BCA team project using **Python Flask** and **SQLite**, the system streamlines venue reservations and booking management for customers and administrators.


##  Features

###  User Module
- User Registration and Login with secure password hashing
- Password Reset
- Browse **AC** and **Non-AC** Function Halls
- View Hall Details, Images, Capacity and Facilities
- Check Hall Availability Before Booking
- Book Halls for Events and Functions
- Multiple Payment Options:
  - 💳 Credit / Debit Card
  - 📱 UPI
  - 💰 Cash on Delivery
- View Booking History
- Cancel Bookings
- Submit Feedback and Reviews

###  Admin Module
- Secure Admin Authentication (separate session)
- Add New Function Halls with Images
- Manage Hall Information
- View and Manage All Customer Bookings
- Track Payment Records
- View and Manage Customer Feedback
- Hall Deletion Protection for Active Registrations

---

##  Tech Stack

| Category        | Technology                |
|-----------------|---------------------------|
| Backend         | Python 3, Flask           |
| Database        | SQLite (5 databases)      |
| Frontend        | HTML5, CSS3, JavaScript   |
| Authentication  | Werkzeug Password Hashing |
| File Handling   | Flask Upload System       |
| Version Control | Git & GitHub              |

---

##  Project Structure

```
Function_Hall_Booking_Management_System/
├── app.py                        ← Main Flask application (all routes & logic)
├── requirements.txt              ← Python dependencies
│
├── templates/                    ← Jinja2 HTML templates
│   ├── base.html                 ← Shared layout (navbar, flash messages)
│   ├── index.html                ← Public landing page
│   ├── login.html                ← Login page
│   ├── registration.html         ← User registration
│   ├── reset_password.html       ← Password reset
│   ├── dashboard.html            ← User dashboard
│   ├── homepage.html             ← Browse hall types
│   ├── acroom.html               ← AC hall listings
│   ├── nonacroom.html            ← Non-AC hall listings
│   ├── hallreg.html              ← Hall booking form
│   ├── payment.html              ← Payment page
│   ├── history.html              ← User booking history
│   ├── feedback.html             ← Submit feedback
│   ├── contact.html              ← Contact information
│   ├── mainpage.html             ← Admin dashboard
│   ├── addhall.html              ← Admin: add hall
│   ├── hallsdetail.html          ← Admin: manage/delete halls
│   ├── registered.html           ← Admin: all customer bookings
│   ├── reghall.html              ← Admin: registrations list
│   ├── payments.html             ← Admin: payment records
│   └── feedbacks.html            ← Admin: customer feedback
│
├── static/
│   ├── css/style.css             ← Stylesheet
│   ├── js/main.js                ← JavaScript
│   └── uploads/                  ← Hall images (auto-created on run)
│
├── users.db                      ← User accounts
├── halls.db                      ← Hall catalog
├── hall_registrations.db         ← Booking records
├── payments.db                   ← Payment records
└── feedback.db                   ← Customer feedback
```

---

##  Installation

### 1. Clone Repository
```bash
git clone https://github.com/Sah-p/Function_Hall_Booking_Management_System.git
cd Function_Hall_Booking_Management_System
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python app.py
```

### 6. Open in Browser
```
http://127.0.0.1:5000
```

> All 5 SQLite databases are created automatically on first run. No manual setup needed.

---

##  Login Credentials

###  Admin
| Field    | Value          |
|----------|----------------|
| Username | `shubha-mastu` |
| Password | `sm@123`       |
| URL      | `http://127.0.0.1:5000/login` |

###  User
Register a new account at `http://127.0.0.1:5000/registration`

---

##  Database Schema

### `users.db`
| Column   | Type    | Description       |
|----------|---------|-------------------|
| id       | INTEGER | Primary key       |
| username | TEXT    | Unique username   |
| email    | TEXT    | Unique email      |
| password | TEXT    | Hashed password   |

### `halls.db`
| Column         | Type    | Description              |
|----------------|---------|--------------------------|
| id             | INTEGER | Primary key              |
| hall_name      | TEXT    | Name of the hall         |
| location       | TEXT    | Address / location       |
| hall_capacity  | INTEGER | Maximum persons          |
| hall_type      | TEXT    | `Ac Hall` / `Non-Ac Hall`|
| meal_type      | TEXT    | Veg / Non-Veg / Both     |
| hall_image     | TEXT    | Image filename           |
| advance_payment| INTEGER | Advance amount (₹)       |

### `hall_registrations.db`
| Column    | Type    | Description        |
|-----------|---------|--------------------|
| id        | INTEGER | Primary key        |
| date      | TEXT    | Booking date       |
| day       | TEXT    | Day of week        |
| hall_name | TEXT    | Booked hall        |
| username  | TEXT    | Booked by          |
| address   | TEXT    | Customer address   |
| contact   | TEXT    | Contact number     |
| purpose   | TEXT    | Event purpose      |

### `payments.db`
| Column          | Type    | Description            |
|-----------------|---------|------------------------|
| id              | INTEGER | Primary key            |
| name            | TEXT    | Username               |
| amount          | REAL    | Amount paid (₹)        |
| payment_method  | TEXT    | Card / UPI / COD       |
| card_number     | TEXT    | Card number (if card)  |
| expiration_date | TEXT    | Card expiry            |
| cvv             | TEXT    | CVV                    |
| billing_address | TEXT    | Billing address        |
| upi_id          | TEXT    | UPI ID (if UPI)        |

### `feedback.db`
| Column   | Type    | Description      |
|----------|---------|------------------|
| id       | INTEGER | Primary key      |
| name     | TEXT    | Customer name    |
| feedback | TEXT    | Feedback message |

---

##  Application Routes

### Public Routes
| Route             | Description            |
|-------------------|------------------------|
| `/`               | Landing page           |
| `/login`          | Login                  |
| `/registration`   | Register new account   |
| `/reset_password` | Reset password         |
| `/logout`         | Logout                 |

### User Routes *(Login Required)*
| Route                            | Description            |
|----------------------------------|------------------------|
| `/dashboard`                     | User dashboard         |
| `/homepage`                      | Browse hall types      |
| `/acroom.html`                   | AC hall listings       |
| `/nonacroom.html`                | Non-AC hall listings   |
| `/hallreg.html`                  | Book a hall            |
| `/payment`                       | Make payment           |
| `/history.html`                  | My bookings            |
| `/cancel-registration/<id>`      | Cancel a booking       |
| `/feedback.html`                 | Submit feedback        |
| `/contact.html`                  | Contact info           |

### Admin Routes *(Admin Login Required)*
| Route                            | Description            |
|----------------------------------|------------------------|
| `/admin`                         | Admin dashboard        |
| `/addhall.html`                  | Add new hall           |
| `/hallsdetail.html`              | Manage/delete halls    |
| `/registered.html`               | All customer bookings  |
| `/reghall.html`                  | Registrations list     |
| `/payments.html`                 | Payment records        |
| `/feedbacks.html`                | Customer feedback      |

---

##  Future Enhancements

- Online Payment Gateway Integration (Razorpay / PayU)
- Email & SMS Notifications on Booking Confirmation
- Real-Time Availability Updates
- AI-Based Hall Recommendations
- Mobile Application Support
- Booking Analytics Dashboard

---

##  Learning Outcomes

This project provided hands-on experience in:
- Full-Stack Web Development with Flask
- Relational Database Management with SQLite
- User Authentication and Session Management
- File Upload Handling
- REST API Design (JSON endpoints)
- Frontend-Backend Integration
- Version Control with Git & GitHub
- Software Project Development as a Team

---

##  License

This project is developed for **academic and educational purposes** as part of the BCA curriculum.
