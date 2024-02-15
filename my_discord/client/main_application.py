from tkinter import messagebox

import customtkinter as ctk
import mysql.connector

from .startup_page import StartupPage
from .login_page import LoginPage
from .create_account_page import CreateAccountPage
from .main_gui import MainGUI

ctk.set_appearance_mode("dark")

db_connection = mysql.connector.connect(
    host="SENSITIVE_DATA",
    user="user",
    password="discord",
    port="SENSITIVE_DATA",
    database="discord"
)

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Battias')

        self.container = ctk.CTkFrame(self, width=400, height=500)
        self.container.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.frames = {}
        for F in (StartupPage, LoginPage, CreateAccountPage): 
            page_name = F.__name__
            frame = F(parent=self.container, controller=self, db_connection=db_connection)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("StartupPage")

    def show_frame(self, page_name):
        if page_name == "MainGUI" and page_name not in self.frames:
            F = MainGUI 
            frame = F(parent=self.container, controller=self, db_connection=db_connection)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)
        else:
            frame = self.frames[page_name]
        frame.tkraise()

        if page_name == "MainGUI":
            self.geometry('1000x600')
            self.container.configure(width=1000, height=600) 
        else:
            self.geometry('600x600') 
            self.container.configure(width=400, height=500) 

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
