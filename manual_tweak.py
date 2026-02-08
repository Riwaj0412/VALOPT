import customtkinter as ctk
import ux
import nvidia_control
import windows_control
import valorant_manager
import threading
import time


class ManualTweakScreen(ctk.CTkFrame):
    def __init__(self, master_app, on_back):
        super().__init__(master_app, fg_color="#0f1923")
        self.app = master_app
        self.on_back = on_back
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title Section
        ctk.CTkLabel(self, text="MANUAL TWEAKS", font=ux.get_font(50),
                     text_color="#ff4655").pack(pady=(80, 40))

        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(expand=True)

        # --- IN GAME SETTINGS BUTTON ---
        self.in_game_btn = ctk.CTkButton(
            self.btn_frame,
            text="[ IN GAME SETTINGS ]",
            font=ux.get_font(22),
            fg_color="transparent",
            border_color="#00f2ff",
            border_width=2,
            text_color="#00f2ff",
            height=80,
            width=450,
            command=self.handle_game_launch
        )
        self.in_game_btn.pack(pady=15)

        # NVIDIA Button [cite: 22, 24]
        ctk.CTkButton(
            self.btn_frame, text="[ NVIDIA CONTROL PANEL ]", font=ux.get_font(22),
            fg_color="transparent", border_color="#76b900", border_width=2,
            text_color="#76b900", height=80, width=450,
            command=lambda: nvidia_control.launch()
        ).pack(pady=15)

        # Windows Button [cite: 22, 30]
        ctk.CTkButton(
            self.btn_frame, text="[ WINDOWS GRAPHICS SETTINGS ]", font=ux.get_font(22),
            fg_color="transparent", border_color="#0078d4", border_width=2,
            text_color="#0078d4", height=80, width=450,
            command=lambda: windows_control.launch()
        ).pack(pady=15)

        # Back Button [cite: 22]
        ctk.CTkButton(self, text="< BACK TO HUB", font=ux.get_font(14),
                      command=self.on_back,
                      fg_color="transparent", text_color="gray").pack(pady=40)

    def handle_game_launch(self):
        """Disables button and starts monitoring process."""
        if valorant_manager.launch_valorant():
            # Update UI to "Pressed/Active" state
            self.in_game_btn.configure(
                state="disabled",
                text="[ GAME RUNNING... ]",
                fg_color="#1a3a3d"  # Darker color to indicate active state
            )
            # Start background thread so UI doesn't freeze
            threading.Thread(target=self.monitor_game_state,
                             daemon=True).start()

    def monitor_game_state(self):
        """Background loop that waits for Valorant to close."""
        # Initial wait for the game process to appear
        time.sleep(15)

        while True:
            if not valorant_manager.is_valorant_running():
                # Game is closed, reset the button via the main thread
                self.after(0, self.reset_button)
                break
            time.sleep(5)  # Poll every 5 seconds

    def reset_button(self):
        """Restores the button to its clickable state."""
        self.in_game_btn.configure(
            state="normal",
            text="[ IN GAME SETTINGS ]",
            fg_color="transparent"
        )
