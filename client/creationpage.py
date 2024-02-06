import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

class CreateAccountPage(ctk.CTkFrame):
    def __init__(self, parent, controller, db_connection):
        super().__init__(parent)
        self.controller = controller
        self.db_connection = db_connection  # Pass the database connection

        # Title
        ctk.CTkLabel(self, text="Create Account", font=("Arial", 24)).pack(pady=20)

        # Name Entry
        self.name_label = ctk.CTkLabel(self, text="Name")
        self.name_label.pack(pady=(10, 0))
        self.name_entry = ctk.CTkEntry(self, width=200, placeholder_text="Name")
        self.name_entry.pack()

        # Last Name Entry
        self.lastname_label = ctk.CTkLabel(self, text="Last Name")
        self.lastname_label.pack(pady=(10, 0))
        self.lastname_entry = ctk.CTkEntry(self, width=200, placeholder_text="Last Name")
        self.lastname_entry.pack()

        # Email Entry
        self.email_label = ctk.CTkLabel(self, text="Email")
        self.email_label.pack(pady=(10, 0))
        self.email_entry = ctk.CTkEntry(self, width=200, placeholder_text="Email")
        self.email_entry.pack()

        # Password Entry
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=(10, 0))
        self.password_entry = ctk.CTkEntry(self, width=200, placeholder_text="Password", show="*")
        self.password_entry.pack()

        # Verify Password Entry
        self.verify_password_label = ctk.CTkLabel(self, text="Verify Password")
        self.verify_password_label.pack(pady=(10, 0))
        self.verify_password_entry = ctk.CTkEntry(self, width=200, placeholder_text="Verify Password", show="*")
        self.verify_password_entry.pack()

        # Create Account Button
        self.create_account_button = ctk.CTkButton(self, text="Create Account", command=self.attempt_create_account)
        self.create_account_button.pack(pady=20)

        # Back Button
        self.back_button = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame("HomePage"))
        self.back_button.pack()

    def is_valid_password(self, password):
        # Check if the password meets the specified criteria
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(not char.isalnum() for char in password)

        return has_uppercase and has_lowercase and has_digit and has_special

    def attempt_create_account(self):
        name = self.name_entry.get()
        lastname = self.lastname_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        verify_password = self.verify_password_entry.get()

        if email and password and verify_password:
            if password == verify_password:
                if self.is_valid_password(password):
                    # Combine name and lastname to create the username
                    username = name + lastname

                    # Insert user data into the database
                    cursor = self.db_connection.cursor()
                    insert_query = "INSERT INTO account (username, name, lastname, email, password) VALUES (%s, %s, %s, %s, %s)"
                    user_data = (username, name, lastname, email, password)
                    cursor.execute(insert_query, user_data)
                    self.db_connection.commit()
                    cursor.close()

                    messagebox.showinfo("Account Created", "Your account has been created successfully.")
                else:
                    messagebox.showerror("Invalid Password", "Password must have one uppercase, one lowercase, one number, and one special character.")
            else:
                messagebox.showerror("Password Mismatch", "Passwords do not match. Please re-enter.")
        else:
            messagebox.showerror("Creation Failed", "Please fill in all fields.")
