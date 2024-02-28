import hashlib

import mysql.connector


def is_valid_password(password):
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    return (
        has_uppercase and
        has_lowercase and
        has_digit and
        has_special
    )


def hash_password(password):
    bytes_password = password.encode() 
    sha256 = hashlib.sha256()
    sha256.update(bytes_password)
    hashed_password = sha256.hexdigest()
    return hashed_password


def attempt_create_account(
    db_connection,
    name,
    last_name,
    email,
    password,
    verify_password
):
    if not (email and password and verify_password):
        return (
            "Creation Failed",
            "Please fill in all fields."
        )

    if password != verify_password:
        return (
            "Password Mismatch",
            "Passwords do not match. Please re-enter."
        )

    if not is_valid_password(password):
        return (
            "Invalid Password",
            "Password must have one uppercase, "
            "one lowercase, one number, "
            "and one special character.",
        )

    # Combine name and lastname to create the username
    username = name + last_name
    password = hash_password(password)

    # Insert user data into the database
    cursor = db_connection.cursor()
    insert_query = (
        "INSERT INTO account "
        "(username, name, lastname, email, password) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    user_data = (username, name, last_name, email, password)
    cursor.execute(insert_query, user_data)
    db_connection.commit()
    cursor.close()

    return (
        "Account Created",
        "Your account has been created successfully."
    )
