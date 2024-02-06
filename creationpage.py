import customtkinter as ctk
from tkinter import messagebox

class CreateAccountPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title
        ctk.CTkLabel(self, text="Create Account", font=("Arial", 24)).pack(pady=20)

        # Name Entry
        self.name_label = ctk.CTkLabel(self, text="Name")
        self.name_label.pack(pady=(10,0))
        self.name_entry = ctk.CTkEntry(self, width=200, placeholder_text="Name")
        self.name_entry.pack()

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

        # Create Account Button
        self.create_account_button = ctk.CTkButton(self, text="Create Account", command=self.attempt_create_account)
        self.create_account_button.pack(pady=20)

        # Back Button
        self.back_button = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        self.back_button.pack()

    def attempt_create_account(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        # içi la logique pour ajouter un compte (il faut mettre en place la db) pour l'instant un placeholder
        if email and password:
            messagebox.showinfo("Account Created", "Your account has been created successfully.")
        else:
            messagebox.showerror("Creation Failed", "Please fill in all fields.")
