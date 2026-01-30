import customtkinter as ctk
from splash import SplashScreen
import dashboard
import engine
import ux


class ValOptApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VALOPT // PRO HUD")

        # Dimensions & Centering
        self.app_width = 1000
        self.app_height = 850
        self.center_window(self.app_width, self.app_height)
        self.resizable(False, False)

        self.node_widgets = {}
        self.is_revealed = False
        self.stored_data = {}

        # Step 1: Start Splash Screen
        self.show_splash()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def show_splash(self):
        self.splash_frame = SplashScreen(self, self.show_detected_screen)

    def show_detected_screen(self, data):
        self.stored_data = data
        game_found = engine.check_valorant_presence()

        status_text = "VALORANT DETECTED" if game_found else "VALORANT NOT FOUND"
        status_color = "#00ff7f" if game_found else "#ff4655"
        sub_text = "CLICK ANYWHERE TO CONTINUE"

        for child in self.winfo_children():
            child.destroy()

        det_frame = ctk.CTkFrame(self, fg_color="#0f1923")
        det_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        ctk.CTkLabel(det_frame, text=status_text, font=ux.get_font(50),
                     text_color=status_color).pack(pady=(350, 10))
        ctk.CTkLabel(det_frame, text=sub_text, font=ux.get_font(18),
                     text_color="white").pack()

        det_frame.bind("<Button-1>", lambda e: self.launch_dashboard())
        for child in det_frame.winfo_children():
            child.bind("<Button-1>", lambda e: self.launch_dashboard())

    def launch_dashboard(self):
        for child in self.winfo_children():
            child.destroy()
        dashboard.build_dashboard(self, self)


if __name__ == "__main__":
    app = ValOptApp()
    app.mainloop()
