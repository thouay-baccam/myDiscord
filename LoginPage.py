import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import hashlib
import MainGUI

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller, db_connection):
        super().__init__(parent)
        self.controller = controller
        self.db_connection = db_connection  # Pass the database connection

        # Title
        ctk.CTkLabel(self, text="Login", font=("Arial", 24)).pack(pady=20)

        # Email Entry
        self.email_label = ctk.CTkLabel(self, text="Email")
        self.email_label.pack(pady=(10,0))
        self.email_entry = ctk.CTkEntry(self, width=200, placeholder_text="Email")
        self.email_entry.pack()

        # Password Entry
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=(10,0))
        self.password_entry = ctk.CTkEntry(self, width=200, placeholder_text="Password", show="*")
        self.password_entry.pack()

        # Login Button
        self.login_button = ctk.CTkButton(self, text="Login", command=self.attempt_login)
        self.login_button.pack(pady=20)

        # Back Button
        self.back_button = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame("StartupPage"))
        self.back_button.pack()

    def attempt_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Query the database to check if the email and hashed password match
        cursor = self.db_connection.cursor()
        select_query = "SELECT * FROM account WHERE email = %s AND password = %s"
        user_data = (email, hashed_password)
        cursor.execute(select_query, user_data)
        result = cursor.fetchone()
        cursor.close()

        if result:
            messagebox.showinfo("Login Successful", "You have been logged in.")
            self.controller.username = result[1]  # Store the username in the MainApplication class
            # Show the MainGUI frame
            self.controller.show_frame("MainGUI")
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")