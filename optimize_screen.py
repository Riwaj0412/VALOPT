import customtkinter as ctk
import ux
from manual_tweak import ManualTweakScreen  # Make sure to import the new class


class OptimizeScreen(ctk.CTkFrame):
    def __init__(self, master_app, on_back):
        super().__init__(master_app, fg_color="#0f1923")
        self.app = master_app  # Store the app reference
        self.on_back = on_back
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.title = ctk.CTkLabel(self, text="OPTIMIZATION HUB",
                                  font=ux.get_font(50), text_color="#ff4655")
        self.title.pack(pady=(100, 50))

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(expand=True)

        self.auto_btn = ctk.CTkButton(
            self.btn_frame, text="[ AUTO OPTIMIZE ]", font=ux.get_font(22),
            fg_color="#ff4655", height=80, width=400, command=self.run_auto
        )
        self.auto_btn.pack(pady=20)

        # UPDATED BUTTON: Change command to self.show_manual
        self.manual_btn = ctk.CTkButton(
            self.btn_frame, text="[ MANUAL TWEAK ]", font=ux.get_font(22),
            fg_color="transparent", border_color="#ff4655", border_width=2,
            height=80, width=400, command=self.show_manual
        )
        self.manual_btn.pack(pady=20)

        self.back_btn = ctk.CTkButton(
            self, text="< BACK TO DASHBOARD", font=ux.get_font(14),
            fg_color="transparent", text_color="gray", command=self.on_back
        )
        self.back_btn.pack(side="bottom", pady=40)

    # NEW FUNCTION: Clears this screen and loads ManualTweakScreen
    def show_manual(self):
        for child in self.winfo_children():
            child.destroy()
        ManualTweakScreen(self.app, lambda: self.app.show_optimize())

    def run_auto(self):
        print("Running Auto Optimization...")
