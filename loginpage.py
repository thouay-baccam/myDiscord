import customtkinter as ctk
from tkinter import messagebox

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

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
        self.back_button = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame("HomePage"))
        self.back_button.pack()

    def attempt_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        # içi la logique pour ce login, pour l'instant un placeholder.
        if email == "user@example.com" and password == "password123":
            messagebox.showinfo("Login Successful", "You have been logged in.")
            # Et ajouter la transition vers interfaceapplication
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")
