import customtkinter as ctk
import ux
from toggle_logic import toggle_specs


class DashboardHUD(ctk.CTkFrame):
    def __init__(self, master_app):
        super().__init__(master_app, fg_color="#0f1923")
        self.app = master_app
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.is_revealed = False
        self.node_widgets = {}

        self.title_label = ctk.CTkLabel(self, text="V A L O P T",
                                        font=ux.get_font(70), text_color="#ff4655")
        self.title_label.pack(pady=(60, 20))

        self.grid_container = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_container.grid_columnconfigure((0, 1), weight=1)

        nodes = [
            ("CORE PROCESSOR", "🖥️", "cpu"), ("SYSTEM MEMORY", "⚡", "ram"),
            ("OS KERNEL", "💾", "os"), ("GRAPHICS CARD", "🎮", "gpu"),
            ("DISPLAY MONITOR", "📺", "monitor"), ("ENGINE STATUS", "🚀", "status")
        ]

        for i, (title, icon, key) in enumerate(nodes):
            node = ux.SpecNode(self.grid_container, title, icon, "DATA LOCKED")
            node.grid(row=i//2, column=i % 2, padx=20, pady=15, sticky="nsew")
            self.node_widgets[key] = node

        # Button frame starts centered
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(expand=True)

        self.reveal_btn = ctk.CTkButton(self.btn_frame, text="[ REVEAL SPECS ]",
                                        font=ux.get_font(22), height=70, width=300,
                                        command=lambda: toggle_specs(self))
        self.reveal_btn.pack(side="left", padx=20)

        self.opt_btn = ctk.CTkButton(self.btn_frame, text="[ OPTIMIZE ]",
                                     font=ux.get_font(22), fg_color="#ff4655",
                                     height=70, width=300)
        self.opt_btn.pack(side="left", padx=20)
