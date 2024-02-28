# startup_page.py

import customtkinter as ctk


class StartupPage(ctk.CTkFrame):
    def __init__(self, parent, controller, db_connection=None):
        super().__init__(parent)
        self.controller = controller
        self.db_connection = db_connection

        ctk.CTkLabel(
            self,
            text="Welcome to Battias",
            font=("Arial", 24)
        ).pack(pady=(20, 5))
        ctk.CTkLabel(
            self,
            text="We're totally better than Discord",
            font=("Arial", 14)
        ).pack(pady=(0, 20))

        ctk.CTkButton(
            self,
            text="Login",
            command=lambda: controller.show_frame("LoginPage")
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="Create Account",
            command=lambda: controller.show_frame("CreateAccountPage"),
        ).pack(pady=10)
