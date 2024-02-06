import customtkinter as ctk
from startpage import StartPage
from loginpage import LoginPage
from creationpage import CreateAccountPage

ctk.set_appearance_mode("dark")  #"Light"/"Dark"
ctk.set_default_color_theme("green")

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Battias')
        self.geometry('600x600')

        self.container = ctk.CTkFrame(self, width=400, height=400)
        self.container.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.frames = {}
        for F in (StartPage, LoginPage, CreateAccountPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()