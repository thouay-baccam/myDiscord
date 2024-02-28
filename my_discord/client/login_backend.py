# login_backend.py

# Standard library
import hashlib


def hash_password(password):
    sha256 = hashlib.sha256()
    bytes_password = password.encode()
    sha256.update(bytes_password)
    hashed_password = sha256.hexdigest()
    return hashed_password


def check_login(db_connection, email, hashed_password):
    cursor = db_connection.cursor()

    cursor.execute(
        f"SELECT * FROM account "
        f"WHERE email = '{email}' "
        f"AND password = '{hashed_password}'"
    )
    result = cursor.fetchone()
    cursor.close()

    return result