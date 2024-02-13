import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from .homepage import HomePage
from .loginpage import LoginPage
from .creationpage import CreateAccountPage


class MainApplication(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="CV&$i7mx$oZDrq", # Modify this for your local setup
            database="discord"
        )
        super().__init__()
        self.title('Battias')
        self.geometry('600x600')

        self.container = ctk.CTkFrame(self, width=400, height=500)
        self.container.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.frames = {}
        for F in (HomePage, LoginPage, CreateAccountPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self, db_connection=db_connection)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()