# MainGUI.py
import customtkinter as ctk
from ChatBackend import ChatBackend
from MemberList import MemberList
import datetime
from ChannelList import ChannelList


class MainGUI(ctk.CTkFrame):  # Inherit from ctk.CTkFrame
    def __init__(self, parent, controller, db_connection):  # Add parent, controller, and db_connection as arguments
        ctk.set_appearance_mode("dark")
        super().__init__(parent)
        self.controller = controller
        self.db_connection = db_connection
        self.backend = ChatBackend(self, controller.username)  # Pass the MainGUI instance to ChatBackend
        self.controller.bind('<Return>', lambda event: self.send_message())
        self.controller.configure(bg='black')

        
        # Create a textbox widget
        self.textbox = ctk.CTkTextbox(self, width=470, height=440)
        self.textbox.place(x=265, y=50)

        # Create an entry widget
        self.entry = ctk.CTkEntry(self, width=400)
        self.entry.place(x=265, y=500)

        # Create a send button 
        self.send_button = ctk.CTkButton(self, text="Send", width=70, height=30, command=self.send_message)
        self.send_button.place(x=672, y=500)

        # Create a connect button
        self.connect_button = ctk.CTkButton(self, text="Connect", width=70, height=30)
        self.connect_button.place(x=100, y=520)

        # Create a disconnect button
        self.disconnect_button = ctk.CTkButton(self, text="Disconnect", width=70, height=20, command=self.disconnect)
        self.disconnect_button.place(x=820, y=570)

        # Create scrollable frames/lists + labels
        self.voice_channels = ctk.CTkScrollableFrame(self, width=200, height=100)
        self.voice_channels.place(x=30, y=50)
        self.voice_label = ctk.CTkLabel(self, text="Voice Channels", width=200)
        self.voice_label.place(x=30, y=20)

        self.text_channels = ctk.CTkScrollableFrame(self, width=200, height=100)
        self.text_channels.place(x=30, y=300)
        self.text_label = ctk.CTkLabel(self, text="Text Channels", width=200)
        self.text_label.place(x=30, y=270)

        self.channel_list = ChannelList(db_connection)
        self.update_channel_list()

        self.members_list = ctk.CTkScrollableFrame(self, width=200, height=470)
        self.members_list.place(x=750, y=50)
        self.members_label = ctk.CTkLabel(self, text="Members List", width=200)
        self.members_label.place(x=750, y=20)

        self.member_list = MemberList(db_connection)
        self.update_member_list()

        # Create a labelbox that will change dynamically (for usernames)
        self.dynamic_label = ctk.CTkLabel(self, text=controller.username, width=200)  # Set the text to the username
        self.dynamic_label.place(x=760, y=540)

        # Keep track of the currently highlighted label
        self.highlighted_label = None

    def on_member_click(self, event):
        # Remove highlight from the previously clicked label
        if self.highlighted_label:
            self.highlighted_label.config(fg="white")  # Change color back to black

        # Highlight the clicked member's name
        clicked_label = event.widget
        clicked_label.config(fg="green")  # You can customize the color
        self.highlighted_label = clicked_label

        # Create a context menu for assigning roles
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Assign roles", command=self.open_role_assignment_window)

        # Show the context menu at the clicked position
        menu.post(event.x_root, event.y_root)

    def open_role_assignment_window(self):
        # Implement your logic for role assignment window here
        # You can create a new Toplevel window and add widgets for role assignment
        pass

    def connect_to_channel(self, port):
        self.backend.connect(port)
        
    def select_channel(self, event, channel, port):
        ...
        # Bind the connect button to the selected channel
        self.connect_button.bind("<Button-1>", lambda event: self.connect_to_channel(port))


    def update_channel_list(self):
        # Get all channels
        channels = self.channel_list.get_channels()

        # Clear the text_channels
        for widget in self.text_channels.winfo_children():
            widget.destroy()

        # Add each channel to the text_channels
        for channel, port in channels:
            label = ctk.CTkLabel(self.text_channels, text=channel)
            label.bind("<Button-1>", lambda event, channel=channel, port=port: self.select_channel(event, channel, port))
            label.pack()

    def update_member_list(self):
        # Get all usernames
        usernames = self.member_list.get_usernames()

        # Clear the members_list
        for widget in self.members_list.winfo_children():
            widget.destroy()

        # Add each username to the members_list
        for username in usernames:
            label = ctk.CTkLabel(self.members_list, text=username)
            label.bind("<Button-1>", self.on_member_click)  # Bind click event
            label.pack()


    def disconnect(self):
        self.backend.client_socket.close()  # Close the socket connection
        self.controller.quit()  # Close the application

    def send_message(self, message=None):
        # Get the message from the entry if not provided
        message = message or self.entry.get()
        # Send the message through the ChatBackend
        self.backend.send_message(message)
        # Clear the entry after sending the message
        self.entry.delete(0, 'end')