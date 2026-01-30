import customtkinter as ctk
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
ASSETS_PATH = os.path.join(BASE_PATH, "assets")


def get_font(size):
    # Matches your exact filename: gaming_font.ttf.ttf
    font_path = os.path.join(ASSETS_PATH, "gaming_font.ttf.ttf")
    if os.path.exists(font_path):
        return ctk.CTkFont(family=font_path, size=size)
    return ("Arial", size, "bold")


class SpecNode(ctk.CTkFrame):
    def __init__(self, master, title, icon, value, **kwargs):
        super().__init__(master, fg_color="#0a0a0a", border_color="#ff4655",
                         border_width=2, corner_radius=12, **kwargs)

        ctk.CTkLabel(self, text=icon, font=("Arial", 35)).pack(pady=(20, 5))
        ctk.CTkLabel(self, text=title, font=get_font(
            20), text_color="#ff4655").pack()

        self.val_label = ctk.CTkLabel(self, text=str(value), font=("Consolas", 12),
                                      text_color="white", wraplength=250)
        self.val_label.pack(pady=(5, 20))

    def update_value(self, new_value):
        self.val_label.configure(text=str(new_value))
