from tkinter import Tk, Canvas, Entry, Text, Button

class ChatUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Battias")
        self.master.geometry("950x600")
        self.master.configure(bg="#242424")
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(
            self.master,
            bg="#242424",
            height=600,
            width=950,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.draw_layout()
        self.create_typing_area()
        self.create_buttons()
        self.create_chat_area()

    def draw_layout(self):
        # Rectangles for layout
        self.canvas.create_rectangle(217, 51, 733, 493, fill="#FFFFFF", outline="")
        self.canvas.create_rectangle(22, 300, 192, 493, fill="#FFFFFF", outline="")
        self.canvas.create_rectangle(22, 51, 192, 244, fill="#FFFFFF", outline="")
        self.canvas.create_rectangle(758, 504, 928, 548, fill="#FFFFFF", outline="")
        self.canvas.create_rectangle(758, 51, 928, 495, fill="#FFFFFF", outline="")

        # Labels above
        self.canvas.create_text(57.0, 28.0, anchor="nw", text="TEXT CHANNELS", fill="#D9D9D9", font=("Inter", 12 * -1))
        self.canvas.create_text(803.0, 31.0, anchor="nw", text="MEMBER LIST", fill="#D9D9D9", font=("Inter", 12 * -1))
        self.canvas.create_text(55.0, 273.0, anchor="nw", text="VOICE CHANNELS", fill="#D9D9D9", font=("Inter", 12 * -1))
    
    def create_chat_area(self):
        # Widget to display sent/received messages
        self.text_1 = Text(self.master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.text_1.place(x=217.0, y=51.0, width=516.0, height=442.0)

    def create_typing_area(self):
        # Entry to send messsages
        self.entry_1 = Entry(self.master, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=217.0, y=504.0, width=431.0, height=35.0)

    def create_buttons(self):
        # Buttons with labels
        self.button_1 = Button(self.master, text="SEND", command=self.send_clicked, relief="flat")
        self.button_1.place(x=661.0, y=504.0, width=72.0, height=37.0)

        self.button_2 = Button(self.master, text="DISCONNECT", command=self.disconnect_clicked, relief="flat")
        self.button_2.place(x=791.0, y=553.0, width=103.0, height=25.0)

        self.button_3 = Button(self.master, text="CONNECT", command=self.connect_clicked, relief="flat")
        self.button_3.place(x=57.0, y=505.0, width=103.0, height=25.0)

    # Event handlers for buttons
    def send_clicked(self):
        print("Send clicked")

    def disconnect_clicked(self):
        print("Disconnect clicked")

    def connect_clicked(self):
        print("Connect clicked")

if __name__ == "__main__":
    root = Tk()
    app = ChatUI(root)
    root.mainloop()
