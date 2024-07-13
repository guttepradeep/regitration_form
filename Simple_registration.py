import mysql.connector

# Function to validate the email format
def validate_email(email):
    if "@" not in email or "." not in email:
        return False
    local, domain = email.split("@")
    if not local or not domain or "." not in domain:
        return False
    return True

# Function to validate the password rules
def validate_password(password):
    if len(password) < 6 or len(password) > 15:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password) # alphanumeric-isalnum() meaning they are either letters (a-z, A-Z) or numbers (0-9).
    return has_upper and has_lower and has_digit and has_special

# Function to connect to the database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pradeepgutte"
    )

# Function to initialize the database
def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (email VARCHAR(255) PRIMARY KEY, password VARCHAR(255))''')
    conn.commit()
    conn.close()

# Function to register a new user
def register(email, password):
    if not validate_email(email):
        print("Invalid email format.")
        return
    if not validate_password(password):
        print("Password must be 6-15 characters long, and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    if user:
        print("Email already registered.")
    else:
        cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        conn.commit()
        print("Registration successful!")
    conn.close()

# Function to log in an existing user
def login(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login successful!")
    else:
        print("Invalid credentials.")
        register_prompt = input("Do you want to register? (yes/no): ")
        if register_prompt.lower() == "yes":
            email = input("Enter email: ")
            password = input("Enter password: ")
            register(email, password)

# Function to handle forgotten passwords
def forgot_password(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
    user = cursor.fetchone() # This method moves the cursor to the next row in the result set and retrieves it.
    conn.close()
    if user:
        print(f"Your password is: {user[0]}")
    else:
        print("Email not found. Please register.")
        email = input("Enter email: ")
        password = input("Enter password: ")
        register(email, password)

# Initialize the database
init_db()

# Simple menu to choose actions
while True:
    print("Choose an action:")
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")

    action = input("Enter your choice (1-4): ")

    if action == "1":
        email = input("Enter email: ")
        password = input("Enter password: ")
        register(email, password)
    elif action == "2":
        email = input("Enter email: ")
        password = input("Enter password: ")
        login(email, password)
    elif action == "3":
        email = input("Enter email: ")
        forgot_password(email)
    elif action == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
