from flask import Flask, render_template, request, redirect,url_for,jsonify,flash,session
import sqlite3
import logging
import os
import re
from werkzeug.utils import secure_filename
import datetime
from datetime import date
from datetime import datetime
from sqlite3 import Error
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'supersecretkey'


# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('/login.html')

@app.route('/reset_password.html')
def reset():
    return render_template('/reset_password.html')

@app.route('/registration.html')
def registration():
    return render_template('/registration.html')

@app.route('/contact.html')
def contact():
    return render_template('/contact.html')

# @app.route('/dashboard.html')
# def dashboard():
#     return render_template('/dashboard.html')

# Function to create the users table if it doesn't exist
def create_users_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE,
                  email TEXT UNIQUE,
                  password TEXT)''')
    conn.commit()
    conn.close()

# Create the users table if it doesn't exist
create_users_table()

# Route to the registration page
@app.route('/registration', methods=['GET', 'POST'])
def registration_page():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect('/registration')
        
        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        # Connect to the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        # Check if username or email already exists
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        if c.fetchone():
            flash('Username already exists. Please choose a different username.', 'error')
            conn.close()
            return redirect('/registration')
        
        c.execute("SELECT * FROM users WHERE email=?", (email,))
        if c.fetchone():
            flash('Email already exists. Please use a different email address.', 'error')
            conn.close()
            return redirect('/registration')
        
        # Insert the user into the database
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
        conn.commit()
        conn.close()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect('/login')
    else:
        return render_template('registration.html')

# Route to the login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

         # Check if the user is admin
        if username == 'shubha-mastu' and password == 'sm@123':
            # Set session variables for admin
            session['logged_in'] = True
            session['username'] = username
            session['is_admin'] = True
            flash('Admin login successful!', 'success')
            conn.close()
            return redirect('/admin')
        

        
        # Check if the user exists
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[3], password):
            # Set session variables
            session['user_id'] = user[0]
            session['username'] = username
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect('/dashboard')
        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect('/login')
    else:
        return render_template('login.html')



# Route to handle resetting the password
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect('/reset_password')

        # Hash the new password
        hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')

        # Connect to the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        # Update the password in the database
        c.execute("UPDATE users SET password=? WHERE email=?", (hashed_password, email))
        if c.rowcount == 0:
            flash('Email not found. Please try again.', 'error')
            conn.close()
            return redirect('/reset_password')
        
        conn.commit()
        conn.close()

        flash('Password reset successfully!', 'success')
        return redirect('/login')
    
    return render_template('reset_password.html')






#Route to the dashboard
@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/login')


# @app.route('/dashboard')
# def dashboard():
#     if session.get('is_user'):
#         return render_template('dashboard.html')
#     else:
#         return redirect('/login')
    
@app.route('/book_now')
def book_now():
    return redirect('/homepage')

# Route for the homepage
@app.route('/homepage')
def homepage():
    # Here you can render your homepage template or return some other response
    return render_template('homepage.html')

# Route to log out
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect('/login')

@app.route('/home')
def home():
     return redirect('/')


@app.route('/admin')
def admin():
    return render_template('mainpage.html')

@app.route('/addhall.html')
def addhall():
    return render_template('addhall.html')

# @app.route('/payments.html')
# def payments():
#     return render_template('payments.html')

@app.route('/feedbacks.html')
def feedbacks():
    return render_template('feedbacks.html')



@app.route('/hallsdetail.html')
def hallsdetail():
    return render_template('hallsdetail.html')

# @app.route('/reghall.html')
# def reg_hall():
#     return render_template('reghall.html')



# # Route to handle the "Book Now" button click
# @app.route('/home')
# def home():
#     # Redirect to the homepage
#     return redirect('/homepage.html')


# # Route for the homepage
# @app.route('/homepage.html')
# def homepage():
#     # Here you can render your homepage template or return some other response
#     return render_template('homepage.html')



@app.route('/hallreg.html')
def hallreg():
    return render_template('hallreg.html')

# @app.route('/make_payment')
# def meke_payment():
#     return redirect('/payment')


# @app.route('/payment.html')
# def payment():
#      return render_template('payment.html')


@app.route('/feedback.html')
def feedback():
    return render_template('feedback.html')

# Ensure the uploads directory exists
# UPLOAD_FOLDER = 'uploads'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = 'uploads/' 
# Route to handle form submission
def create_data():
    conn = sqlite3.connect('halls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS halls 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 hall_name TEXT, location TEXT, hall_capacity INTEGER, 
                 hall_type TEXT, meal_type TEXT, 
                 hall_image TEXT, advance_payment INTEGER)''')
    conn.commit()
    conn.close()

# Create the halls table if it doesn't exist
create_data()


# Route to handle form submission
@app.route('/add_hall', methods=['POST'])
def add_hall():
    
    if request.method == 'POST':
        print('addhall')
        hall_name = request.form['hall_name']
        location = request.form['location']
        hall_capacity = request.form['hall_capacity']
        hall_type = request.form['hall_type']
        meal_type =str(request.form['meal_type'])
        hall_image = request.files['hall_image']
        advance_payment = request.form['advance_payment']
        
         # Print extracted data for debugging
        print("Form Data:")
        print("Hall Name:", hall_name)
        print("Location:", location)
        print("Hall Capacity:", hall_capacity)
        print("Hall Type:", hall_type)
        print("Meal Type:", meal_type)
        print("Advance Payment:", advance_payment)
        print("Hall Image:", hall_image.filename if hall_image else None)

        try:
            # Convert hall_capacity and advance_payment to integers
            hall_capacity = int(hall_capacity)
            advance_payment = int(advance_payment)
            
            # Check for negative values
            if hall_capacity < 0 or advance_payment < 0:
                flash('Capacity and advance payment must be non-negative integers', 'error')
                return redirect('/addhall.html')
        except ValueError:
            flash('Capacity and advance payment must be integers', 'error')
            return redirect('/addhall.html')

        if hall_image.filename != '':
            filename = secure_filename(hall_image.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            hall_image.save(file_path)
        else:
            # Handle case where no file was uploaded
            flash('No file uploaded', 'error')
            return redirect('/addhall.html')
        
        # Handle file upload
        conn = sqlite3.connect('halls.db')
        c = conn.cursor()
        c.execute('''INSERT INTO halls 
                     (hall_name, location,hall_capacity, hall_type, 
                     meal_type, hall_image, advance_payment) 
                     VALUES (?, ?, ?, ?, ?, ?,?)''', 
                     (hall_name, location,hall_capacity, hall_type, 
                     meal_type, filename, advance_payment))
        conn.commit()
        conn.close()
        
         # Flash success message
        flash('Hall information successfully added!', 'success')

        # Redirect to the homepage or wherever you want
        return redirect('/addhall.html')
    else:
        return "Method not allowed"


        
        
    
@app.route('/acroom.html')
def ac_rooms():
    print('acroom')
    # Connect to the database
    conn = sqlite3.connect('halls.db')
    c = conn.cursor()

    # Fetch hall names of AC rooms from the database
    c.execute("SELECT hall_name, hall_image FROM halls WHERE hall_type = 'Ac Hall'")
    hall_data =c.fetchall()

    # Close the database connection
    conn.close()
    hall_names = [{'hall_name': row[0], 'hall_image': row[1]} for row in hall_data]
    # Render the template with the hall names
    print(hall_names)
    return render_template('acroom.html', hall_names=hall_names)

@app.route('/nonacroom.html')
def nonac_rooms():
    # Connect to the database
    conn = sqlite3.connect('halls.db')
    c = conn.cursor()

    # Fetch hall names of AC rooms from the database
    c.execute("SELECT hall_name, hall_image FROM halls WHERE hall_type = 'Non-Ac Hall'")
    hall_data =c.fetchall()

    # Close the database connection
    conn.close()
    hall_names = [{'hall_name': row[0], 'hall_image': row[1]} for row in hall_data]
    # Render the template with the hall names
    print(hall_names)
    return render_template('nonacroom.html', hall_names=hall_names)


@app.route('/hall_details', methods=['POST'])
def hall_details():
    # Get the hall name from the request data
    hall_name = request.json.get('hallName')

    # Connect to the database
    conn = sqlite3.connect('halls.db')
    c = conn.cursor()

    # Fetch all columns for the given hall name
    c.execute("SELECT * FROM halls WHERE hall_name = ?", (hall_name,))
    hall_details = c.fetchone()

    # Close the database connection
    conn.close()

    # Convert the result to a dictionary
    hall_details_dict = {
        'hall_name': hall_details[1],
        'location':hall_details[2],
        'hall_capacity': hall_details[3],
        'hall_type': hall_details[4],
        'meal_type': hall_details[5],
        'advance_payment': hall_details[7]
    }

    # Return hall details as JSON response
    return jsonify(hall_details_dict)

logging.basicConfig(level=logging.INFO)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('hall_registrations.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS registrations
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date TEXT,
                  day TEXT,
                  hall_name TEXT,
                  username TEXT,
                  address TEXT,
                  contact TEXT,
                  purpose TEXT)''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route to handle AJAX request for checking registration
@app.route('/check_registration', methods=['POST'])
def check_registration():
    if 'username' not in session:
        return jsonify({'error': 'User not logged in'}), 401
    try:
        date_str = request.form.get('date')
        day = request.form.get('day')
        hall_name = request.form.get('hall_name')
        
        # Connect to the database
        conn = sqlite3.connect('hall_registrations.db')
        c = conn.cursor()
        
        # Check if registration already exists for the given date, day, and hall
        c.execute('''SELECT COUNT(*) FROM registrations
                     WHERE date = ? AND day = ? AND hall_name = ?''', (date_str, day, hall_name))
        existing_registrations = c.fetchone()[0]
        conn.close()
        
        if existing_registrations > 0:
            return jsonify({'exists': True}), 200
        else:
            return jsonify({'exists': False}), 200

    except sqlite3.Error as e:
        logging.error("SQLite error: %s", e, exc_info=True)
        return jsonify({'error': 'Database error occurred'}), 500

    except Exception as e:
        logging.error("Unexpected error occurred: %s", e, exc_info=True)
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500


# Route to handle form submission for hall registration
@app.route('/hall_reg', methods=['POST'])
def hall_reg():
    if 'username' not in session:
        return jsonify({'error': 'User not logged in'}), 401
    try:
        # Get form data
        form_data = request.form
        date_str = form_data.get('date')
        day = form_data.get('day')
        hall_name = form_data.get('hall_name')
        username = form_data.get('username')
        address = form_data.get('address')
        contact = form_data.get('contact')
        purpose = form_data.get('purpose')
        
        # Check if all required fields are present
        if not all([date_str, day, hall_name, username, address, contact, purpose]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if username != session['username']:
            return jsonify({'error': 'The username provided does not match the logged-in user'}), 400
        
        # Convert date string to datetime object
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        # Get today's date
        current_date = date.today()

        # Check if the selected date is in the past
        if selected_date < current_date:
            return jsonify({'error': 'Please select a date that is not in the past'}), 400

        # Check if the selected date is within the allowed year range (2024)
        if selected_date.year != 2024:
            return jsonify({'error': 'Hall registration is allowed only for the year 2024'}), 400
        
        # Connect to the database
        conn = sqlite3.connect('hall_registrations.db')
        c = conn.cursor()
        
        # Check if registration already exists for the given date, day, and hall
        c.execute('''SELECT COUNT(*) FROM registrations
                     WHERE date = ? AND day = ? AND hall_name = ?''', (date_str, day, hall_name))
        existing_registrations = c.fetchone()[0]
        
        if existing_registrations > 0:
            conn.close()
            return jsonify({'error': 'A registration already exists for this hall on the selected date and day'}), 400
        else:
            # Insert data into the database
            c.execute('''INSERT INTO registrations (date, day, hall_name,username, address, contact,purpose)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''', (date_str, day, hall_name,username, address, contact,purpose))
            conn.commit()  # Commit the transaction
            conn.close()
            
            # Redirect to payment page after successful registration
            return redirect('/payment')

    except sqlite3.Error as e:
        # Log SQLite errors
        print("SQLite error:", e)
        return jsonify('Database error occurred'), 500

    except Exception as e:
    # Log other unexpected errors
        logging.error("Unexpected error occurred:", exc_info=True)
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500


def init_db():
    conn = sqlite3.connect('payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            payment_method TEXT NOT NULL,
            card_number TEXT,
            expiration_date TEXT,
            cvv TEXT,
            billing_address TEXT,
            upi_id TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()



@app.route('/payment')
def payment_page():
    return render_template('payment.html')

@app.route('/payment', methods=['GET','POST'])
def payment():
    if 'username' not in session:
        return jsonify({'success': False, 'message': 'You must be logged in to make a payment.'})
    

    # Retrieve form data
    name = request.form.get('name')
    amount = float(request.form['amount'])
    payment_method = request.form['payment_method']
    card_number = request.form.get('card_number')
    expiration_date = request.form.get('expiration_date')
    cvv = request.form.get('cvv')
    billing_address = request.form.get('billing_address')
    upi_id = request.form.get('upi_id')

    if name != session['username']:
            return jsonify({'success': False, 'message': 'Entered name must match the logged-in username.'})

    conn = sqlite3.connect('payments.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payments (name, amount, payment_method, card_number, expiration_date, cvv, billing_address, upi_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, amount, payment_method, card_number, expiration_date, cvv, billing_address, upi_id))
    conn.commit()
    conn.close()

    home_url = url_for('dashboard')

    if payment_method == 'Cash on Delivery':
        return jsonify({'success': True, 'message': "Amount is ready to be collected.", 'home_url': home_url})

    flash("Payment successful!")
    return jsonify({'success': True, 'message': "Payment successful!", 'home_url': home_url})

   
    
@app.route('/payments.html')
def payments():
    conn = sqlite3.connect('payments.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM payments')
    payments = cursor.fetchall()
    conn.close()
    return render_template('payments.html', payments=payments)



@app.route('/reghall.html')
def reg_hall():
    try:
        conn = sqlite3.connect('hall_registrations.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, date, day, hall_name FROM registrations')
        registrations = cursor.fetchall()
        conn.close()
        return render_template('reghall.html', registrations=registrations)
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "Error accessing database"
    

@app.route('/registered.html')
def registered():
    try:
        conn = sqlite3.connect('hall_registrations.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, date, day, hall_name, username, contact FROM registrations')
        registrations = cursor.fetchall()
        conn.close()
        return render_template('registered.html', registrations=registrations)
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "Error accessing database"
    
@app.route('/delete-registration/<int:registration_id>', methods=['POST'])
def delete_registration(registration_id):
    try:
        conn = sqlite3.connect('hall_registrations.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM registrations WHERE id = ?', (registration_id,))
        conn.commit()
        conn.close()
        # return redirect('registered.html')
        return 'Registration deleted successfully', 200
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "Error deleting registration"



# def get_registrations():
#     conn = sqlite3.connect('hall_registrations.db')
#     c = conn.cursor()
#     c.execute('SELECT id, date, day, hall_name FROM registrations')
#     registrations = c.fetchall()
#     conn.commit()  # Commit changes
#     conn.close()
#     return registrations


# @app.route('/reghall.html')  # This should be the URL associated with the route, not the HTML file name
# def registered_halls():
#     registrations = get_registrations()
#     return render_template('reghall.html', registrations=registrations)

# Function to fetch AC halls from the database
def fetch_ac_halls():
    conn = sqlite3.connect('halls.db')
    cursor = conn.cursor()
    cursor.execute("SELECT hall_name FROM halls WHERE hall_type = 'Ac Hall'")
    ac_halls = [{'hall_name': row[0]} for row in cursor.fetchall()]
    conn.close()
    return ac_halls

# Function to fetch Non-AC halls from the database
def fetch_non_ac_halls():
    conn = sqlite3.connect('halls.db')
    cursor = conn.cursor()
    cursor.execute("SELECT hall_name FROM halls WHERE hall_type = 'Non-Ac Hall'")
    non_ac_halls = [{'hall_name': row[0]} for row in cursor.fetchall()]
    conn.close()
    return non_ac_halls

# Route for fetching halls based on type
@app.route('/hallsdetail', methods=['POST'])
def fetch_halls():
    hall_type = request.form.get('hall_type')
    if not hall_type:
        return jsonify(error="hall_type is required"), 400

    if hall_type == 'Ac Hall':
        halls = fetch_ac_halls()
    else:
        halls = fetch_non_ac_halls()
    return jsonify(halls=halls), 200

# Route to handle delete requests
@app.route('/delete', methods=['POST'])
def delete_hall():
    hall_name = request.form.get('hall_name')
    if not hall_name:
        return jsonify(error="hall_name is required"), 400

    try:
        # Check for existing registrations for the given hall name
        reg_conn = sqlite3.connect('hall_registrations.db')
        reg_cursor = reg_conn.cursor()
        reg_cursor.execute("SELECT COUNT(*) FROM registrations WHERE hall_name = ?", (hall_name,))
        registrations_count = reg_cursor.fetchone()[0]
        reg_conn.close()
        
        if registrations_count > 0:
            return jsonify(error="Cannot delete hall with existing registrations"), 400
        else:
            # Delete the hall since there are no registrations
            hall_conn = sqlite3.connect('halls.db')
            hall_cursor = hall_conn.cursor()
            hall_cursor.execute("DELETE FROM halls WHERE hall_name = ?", (hall_name,))
            hall_conn.commit()
            if hall_cursor.rowcount == 0:
                hall_conn.close()
                return jsonify(error="Hall not found"), 404
            hall_conn.close()
        
    except sqlite3.Error as e:
        return jsonify(error=str(e)), 500

    return jsonify(message="Hall deleted successfully"), 200






DATABASE = 'feedback.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.json
        name = data.get('name')
        feedback = data.get('feedback')

        print("Received data:", name, feedback)

        if not name or not feedback:
            return jsonify({'error': 'Name and feedback are required.'}), 400

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO feedback (name, feedback) VALUES (?, ?)', (name, feedback))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Feedback successfully submitted!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_feedback_data')
def get_feedback_data():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM feedback')
        feedback_data = cursor.fetchall()
        conn.close()
        return jsonify(feedback_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500





DATABASE = 'feedback.db'

def get_db():
    """ Get a database connection """
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/get_feedback')
def get_feedback():
    """ Retrieve feedback data from the database """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, feedback FROM feedback')
    feedback_data = cursor.fetchall()
    conn.close()
    feedback_list = [{'id': row[0], 'name': row[1], 'feedback': row[2]} for row in feedback_data]
    return jsonify(feedback_list)


@app.route('/delete_feedback/<int:id>', methods=['DELETE'])
def delete_feedback(id):
    """ Delete feedback data from the database """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM feedback WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Feedback deleted successfully'}), 200


def get_current_user():
    # Function to get the current logged-in user
    return session.get('username')

@app.route('/history.html')
def history():
    try:
        username = get_current_user()
        if not username:
            return redirect(url_for('login'))  # Redirect to login if user is not logged in

        conn = sqlite3.connect('hall_registrations.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, date, day, hall_name FROM registrations WHERE username = ?', (username,))
        registrations = cursor.fetchall()
        conn.close()
        return render_template('history.html', registrations=registrations)
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "Error accessing database"
    

@app.route('/cancel-registration/<int:registration_id>', methods=['POST'])
def cancel_registration(registration_id):
    try:
        username = get_current_user()
        if not username:
            return redirect(url_for('login'))  # Redirect to login if user is not logged in

        conn = sqlite3.connect('hall_registrations.db')
        cursor = conn.cursor()

        # Check if the registration belongs to the current user
        cursor.execute('SELECT username FROM registrations WHERE id = ?', (registration_id,))
        result = cursor.fetchone()
        if not result or result[0] != username:
            conn.close()
            return "Unauthorized", 403

        cursor.execute('DELETE FROM registrations WHERE id = ?', (registration_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('history'))  # Redirect to the registered page
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return "Error deleting registration"



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
      
        
       

          



    
