# Function Hall Booking Management System

A full-stack web application for browsing, booking, and managing function halls. Built with **Python Flask** and **SQLite** as a BCA team project.

##  Features

###  User Side
- Register & Login with secure password hashing (bcrypt/pbkdf2)
- Password reset by email
- Browse **AC Halls** and **Non-AC Halls** with images and details
- Check hall availability by date before booking
- Book a hall with date, purpose, contact info
- **Payment** via Credit/Debit Card, UPI, or Cash on Delivery
- View booking history and cancel bookings
- Submit feedback

###  Admin Side
- Secure admin login (separate session)
- Add new halls (name, location, capacity, type, meal type, image, advance payment)
- View and delete halls (with registration check protection)
- View all customer bookings
- View all payment records
- Read and delete customer feedback

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Database | SQLite (5 separate DBs) |
| Frontend | HTML5, CSS3, JavaScript |
| Auth | Werkzeug password hashing |
| File Uploads | Flask + Werkzeug secure_filename |

---

##  Project Structure

```
Function_Hall_Booking_Management_System/
├── app.py                        ← Main Flask application (all routes)
├── requirements.txt              ← Python dependencies
│
├── templates/                    ← Jinja2 HTML templates
│   ├── base.html                 ← Shared layout (nav, flash messages)
│   ├── index.html                ← Public landing page
│   ├── login.html                ← User/Admin login
│   ├── registration.html         ← New user registration
│   ├── reset_password.html       ← Password reset
│   ├── dashboard.html            ← User dashboard
│   ├── homepage.html             ← Hall type selection
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
│   ├── registered.html           ← Admin: all bookings
│   ├── reghall.html              ← Admin: registrations list
│   ├── payments.html             ← Admin: payment records
│   └── feedbacks.html            ← Admin: customer feedback
│
├── static/
│   ├── css/style.css             ← All styling
│   ├── js/main.js                ← Flash message auto-dismiss
│   └── uploads/                  ← Hall images (auto-created)
│
├── users.db                      ← User accounts
├── halls.db                      ← Hall catalog
├── hall_registrations.db         ← Booking records
├── payments.db                   ← Payment records
└── feedback.db                   ← Customer feedback
```

---

##  Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Step 1 — Clone the Repository
```bash
git clone https://github.com/Sah-p/Function_Hall_Booking_Management_System.git
cd Function_Hall_Booking_Management_System
```

### Step 2 — Create a Virtual Environment
```bash
python -m venv myenv

# Activate on Windows:
myenv\Scripts\activate

# Activate on Mac/Linux:
source myenv/bin/activate
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the Application
```bash
python app.py
```

### Step 5 — Open in Browser
```
http://127.0.0.1:5000
```

---

##  Login Credentials

###  Admin Login
| Field | Value |
|-------|-------|
| Username | `shubha-mastu` |
| Password | `sm@123` |
| URL | `http://127.0.0.1:5000/login` |

After login, admin is redirected to `/admin` panel.

###  User Login
Register a new account at:
```
http://127.0.0.1:5000/registration
```

---

##  Database Schema

All databases are auto-created on the first run.

### `users.db` — users table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Unique username |
| email | TEXT | Unique email |
| password | TEXT | Hashed password |

### `halls.db` — halls table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| hall_name | TEXT | Name of the hall |
| location | TEXT | Address/location |
| hall_capacity | INTEGER | Max persons |
| hall_type | TEXT | `Ac Hall` or `Non-Ac Hall` |
| meal_type | TEXT | Veg / Non-Veg / Both |
| hall_image | TEXT | Image filename |
| advance_payment | INTEGER | Advance amount (₹) |

### `hall_registrations.db` — registrations table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| date | TEXT | Booking date |
| day | TEXT | Day of week |
| hall_name | TEXT | Booked hall |
| username | TEXT | Booked by |
| address | TEXT | Customer address |
| contact | TEXT | Contact number |
| purpose | TEXT | Event purpose |

### `payments.db` — payments table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name | TEXT | Username |
| amount | REAL | Amount paid (₹) |
| payment_method | TEXT | Card / UPI / COD |
| card_number | TEXT | Card number (if card) |
| expiration_date | TEXT | Expiry (if card) |
| cvv | TEXT | CVV (if card) |
| billing_address | TEXT | Billing address |
| upi_id | TEXT | UPI ID (if UPI) |

### `feedback.db` — feedback table
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name | TEXT | Customer name |
| feedback | TEXT | Feedback message |

---

##  Application Routes

### Public
| Route | Description |
|-------|-------------|
| `/` | Landing page |
| `/login` | Login page |
| `/registration` | Register new account |
| `/reset_password` | Reset password |
| `/logout` | Logout |

### User (Login Required)
| Route | Description |
|-------|-------------|
| `/dashboard` | User dashboard |
| `/homepage` | Browse hall types |
| `/acroom.html` | View AC halls |
| `/nonacroom.html` | View Non-AC halls |
| `/hallreg.html` | Book a hall |
| `/payment` | Make payment |
| `/history.html` | My bookings |
| `/feedback.html` | Submit feedback |
| `/contact.html` | Contact info |

### Admin (Admin Login Required)
| Route | Description |
|-------|-------------|
| `/admin` | Admin dashboard |
| `/addhall.html` | Add new hall |
| `/hallsdetail.html` | Manage halls |
| `/registered.html` | All customer bookings |
| `/reghall.html` | Hall registrations |
| `/payments.html` | Payment records |
| `/feedbacks.html` | Customer feedback |

---

##  Screenshots

> Add screenshots of your project here after running it locally.

---

##  Requirements

```
Flask==2.2.3
Werkzeug==2.2.3
```

---

##  License

This project is developed as a **BCA Academic Team Project**.

---
