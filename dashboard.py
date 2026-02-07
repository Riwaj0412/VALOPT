import customtkinter as ctk
import ux
import launcher
import specs_factory
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

        self.play_container = ctk.CTkFrame(self, fg_color="transparent")
        self.play_container.pack(pady=20)

        self.play_btn = ctk.CTkButton(
            self.play_container, text="[ PLAY ]", font=ux.get_font(22),
            fg_color="transparent", border_color="#00ff7f", border_width=2,
            text_color="#00ff7f", height=70, width=300,
            command=self.handle_play_click
        )
        self.play_btn.pack()

        self.grid_container = ctk.CTkFrame(self, fg_color="transparent")
        specs_factory.build_specs_grid(self.grid_container, self.node_widgets)

        self.setup_footer()

    def setup_footer(self):
        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.pack(side="bottom", pady=60)

        self.reveal_btn = ctk.CTkButton(
            self.footer_frame, text="[ REVEAL SPECS ]", font=ux.get_font(22),
            fg_color="transparent", border_color="#ff4655", border_width=2,
            height=70, width=300, command=lambda: toggle_specs(self)
        )
        self.reveal_btn.pack(side="left", padx=20)

        self.opt_btn = ctk.CTkButton(
            self.footer_frame, text="[ OPTIMIZE ]", font=ux.get_font(22),
            fg_color="#ff4655", height=70, width=300,
            command=self.app.show_optimize
        )
        self.opt_btn.pack(side="left", padx=20)

    def handle_play_click(self):
        self.play_btn.configure(text="[ IN-GAME ]", state="disabled")
        launcher.start_game(self.reset_play_button)

    def reset_play_button(self):
        self.play_btn.configure(text="[ PLAY ]", state="normal")
