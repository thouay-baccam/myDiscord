# create_account_page.py

# Standard library
from tkinter import messagebox

# Third-party libraries
import customtkinter as ctk

# Local modules
from .create_account_backend import attempt_create_account


class CreateAccountPage(ctk.CTkFrame):
    def __init__(self, parent, controller, db_connection):
        super().__init__(parent)
        self.controller = controller
        # Pass the database connection
        self.db_connection = db_connection

        # Title
        ctk.CTkLabel(
            self,
            text="Create Account",
            font=("Arial", 24)
        ).pack(pady=20)

        # Name Entry
        self.name_label = ctk.CTkLabel(self, text="Name")
        self.name_label.pack(pady=(10, 0))
        self.name_entry = ctk.CTkEntry(
            self,
            width=200,
            placeholder_text="Name"
        )
        self.name_entry.pack()

        # Last Name Entry
        self.last_name_label = ctk.CTkLabel(
            self,
            text="Last Name"
        )
        self.last_name_label.pack(pady=(10, 0))
        self.last_name_entry = ctk.CTkEntry(
            self,
            width=200,
            placeholder_text="Last Name"
        )
        self.last_name_entry.pack()

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

        # Verify Password Entry
        self.verify_password_label = ctk.CTkLabel(
            self,
            text="Verify Password"
        )
        self.verify_password_label.pack(pady=(10, 0))
        self.verify_password_entry = ctk.CTkEntry(
            self,
            width=200,
            placeholder_text="Verify Password",
            show="*"
        )
        self.verify_password_entry.pack()

        # Create Account Button
        self.create_account_button = ctk.CTkButton(
            self,
            text="Create Account",
            command=self.show_attempt_create_account
        )
        self.create_account_button.pack(pady=20)

        # Back Button
        self.back_button = ctk.CTkButton(
            self,
            text="Back",
            command=lambda: controller.show_frame("StartupPage")
        )
        self.back_button.pack()

    def show_attempt_create_account(self):
        result = attempt_create_account(
            self.db_connection,
            self.name_entry.get(),
            self.last_name_entry.get(),
            self.email_entry.get(),
            self.password_entry.get(),
            self.verify_password_entry.get()
        )
        messagebox.showinfo(
            result[0],
            result[1]
        )