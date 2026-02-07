import customtkinter as ctk
import ux
import nvidia_control
import windows_control


class ManualTweakScreen(ctk.CTkFrame):
    def __init__(self, master_app, on_back):
        super().__init__(master_app, fg_color="#0f1923")
        self.app = master_app
        self.on_back = on_back
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title
        ctk.CTkLabel(self, text="MANUAL TWEAKS", font=ux.get_font(50),
                     text_color="#ff4655").pack(pady=(80, 40))

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(expand=True)

        # NVIDIA Button - Notice the lambda to fix the 'auto-popup'
        ctk.CTkButton(
            self.btn_frame, text="[ NVIDIA CONTROL PANEL ]", font=ux.get_font(22),
            fg_color="transparent", border_color="#76b900", border_width=2,
            text_color="#76b900", height=80, width=450,
            command=lambda: nvidia_control.launch()
        ).pack(pady=15)

        # Windows Button
        ctk.CTkButton(
            self.btn_frame, text="[ WINDOWS GRAPHICS SETTINGS ]", font=ux.get_font(22),
            fg_color="transparent", border_color="#0078d4", border_width=2,
            text_color="#0078d4", height=80, width=450,
            command=lambda: windows_control.launch()
        ).pack(pady=15)

        # Back Button
        ctk.CTkButton(self, text="< BACK TO HUB", font=ux.get_font(14),
                      fg_color="transparent", text_color="gray",
                      command=self.on_back).pack(side="bottom", pady=40)
