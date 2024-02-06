import customtkinter as ctk

class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Welcome to Battias", font=("Arial", 24)).pack(pady=(20, 5))
        ctk.CTkLabel(self, text="We're totally better than Discord", font=("Arial", 14)).pack(pady=(0, 20))

        ctk.CTkButton(self, text="Login", command=lambda: controller.show_frame("LoginPage")).pack(pady=10)

        ctk.CTkButton(self, text="Create Account", command=lambda: controller.show_frame("CreateAccountPage")).pack(pady=10)
