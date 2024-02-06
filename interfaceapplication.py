# interface.py
import customtkinter as ctk

class InterfaceApplication  (ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Battias Chat Interface")
        self.geometry("900x500")

        # Define primary and secondary colors
        primary_color = "#5c4ac7"  # Replace with your primary color
        secondary_color = "#ffffff"  # Replace with your secondary color
        background_color = "#343434"  # Assuming a dark background based on the image

        # Sidebar for channels
        sidebar_frame = ctk.CTkFrame(self, fg_color=background_color)
        sidebar_frame.pack(side="left")

        text_channel_label = ctk.CTkLabel(sidebar_frame, text="Text Channels", text_color=secondary_color)
        text_channel_label.pack(pady=10)

        voice_channel_label = ctk.CTkLabel(sidebar_frame, text="Voice Channels", text_color=secondary_color)
        voice_channel_label.pack(pady=10)

        # Member list
        member_frame = ctk.CTkFrame(self, fg_color=background_color)
        member_frame.pack(side="right")

        member_list_label = ctk.CTkLabel(member_frame, text="MEMBER LIST", text_color=secondary_color)
        member_list_label.pack(pady=10)

        # Chat box
        chat_frame = ctk.CTkFrame(self, fg_color=background_color)
        chat_frame.pack(side="left", fill="both", expand=True)

        chat_box_label = ctk.CTkLabel(chat_frame, text="CHAT BOX", text_color=secondary_color)
        chat_box_label.pack(pady=10)

        # Create a frame for message entry and send button
        entry_button_frame = ctk.CTkFrame(chat_frame, fg_color=background_color)
        entry_button_frame.pack(side="bottom", fill="x")

        message_entry = ctk.CTkEntry(entry_button_frame, placeholder_text="Type message here", width=500)
        message_entry.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        send_button = ctk.CTkButton(entry_button_frame, text="Send", fg_color=primary_color, text_color=secondary_color)
        send_button.pack(side="left", padx=10)

if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()