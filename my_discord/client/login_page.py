# login_page.py

# Standard library
from tkinter import messagebox

# Third-party libraries
import customtkinter as ctk

# Local modules
from .main_gui import MainGUI
from .login_backend import hash_password, check_login


class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller, db_connection):
        super().__init__(parent)
        self.controller = controller
        # Pass the database connection
        self.db_connection = db_connection

        # Title
        ctk.CTkLabel(
            self,
            text="Login",
            font=("Arial", 24)
        ).pack(pady=20)

        # Email Entry
        self.email_label = ctk.CTkLabel(self, text="Email")
        self.email_label.pack(pady=(10, 0))
        self.email_entry = ctk.CTkEntry(
            self,
            width=200,
            placeholder_text="Email"
        )
        self.email_entry.pack()

        # Password Entry
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=(10, 0))
        self.password_entry = ctk.CTkEntry(
            self,
            width=200,
            placeholder_text="Password",
            show="*"
        )
        self.password_entry.pack()

        # Login Button
        self.login_button = ctk.CTkButton(
            self,
            text="Login",
            command=self.attempt_login
        )
        self.login_button.pack(pady=20)

        # Back Button
        self.back_button = ctk.CTkButton(
            self, text="Back",
            command=lambda: controller.show_frame("StartupPage")
        )
        self.back_button.pack()

    def attempt_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        hashed_password = hash_password(password)
        result = check_login(
            self.db_connection,
            email,
            hashed_password
        )

        if result:
            messagebox.showinfo(
                "Login Successful",
                "You have been logged in."
            )
            # Store the username in the MainApplication class
            self.controller.username = result[1]
            # Show the MainGUI frame
            self.controller.show_frame("MainGUI")
        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid email or password."
            )
