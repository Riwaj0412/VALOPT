import customtkinter as ctk
import ux
from toggle_logic import toggle_specs


def build_dashboard(master, app_instance):
    hud_frame = ctk.CTkFrame(master, fg_color="#0f1923")
    hud_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    app_instance.title_label = ctk.CTkLabel(hud_frame, text="V A L O P T",
                                            font=ux.get_font(70), text_color="#ff4655")
    app_instance.title_label.pack(pady=(60, 20))

    app_instance.grid_container = ctk.CTkFrame(
        hud_frame, fg_color="transparent")
    grid = app_instance.grid_container
    grid.grid_columnconfigure((0, 1), weight=1)

    # Updated Specs List
    nodes = [
        ("CORE PROCESSOR", "🖥️", "cpu"), ("SYSTEM MEMORY", "⚡", "ram"),
        ("OS KERNEL", "💾", "os"), ("GRAPHICS CARD", "🎮", "gpu"),
        ("DISPLAY MONITOR", "📺", "monitor"), ("ENGINE STATUS", "🚀", "status")
    ]

    for i, (title, icon, key) in enumerate(nodes):
        node = ux.SpecNode(grid, title, icon, "DATA LOCKED")
        node.grid(row=i//2, column=i % 2, padx=20, pady=15, sticky="nsew")
        app_instance.node_widgets[key] = node

    # Hero Buttons
    app_instance.btn_frame = ctk.CTkFrame(hud_frame, fg_color="transparent")
    app_instance.btn_frame.pack(expand=True)

    app_instance.reveal_btn = ctk.CTkButton(app_instance.btn_frame, text="[ REVEAL SPECS ]",
                                            font=ux.get_font(22), height=70, width=300,
                                            command=lambda: toggle_specs(app_instance))
    app_instance.reveal_btn.pack(side="left", padx=20)

    app_instance.opt_btn = ctk.CTkButton(app_instance.btn_frame, text="[ OPTIMIZE ]",
                                         font=ux.get_font(22), fg_color="#ff4655",
                                         height=70, width=300)
    app_instance.opt_btn.pack(side="left", padx=20)

    return hud_frame
